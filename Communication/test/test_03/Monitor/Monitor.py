import argparse
from datetime import datetime
import struct
import sys
import time
import traceback

import pigpio
from nrf24 import *

RF24NT_HUB_IP:bytes[1]      = 0b10000000
RF24NT_MONITORS_IP:bytes[1] = 0b10000001  

PRINT_DELAY = 1  # Second

hostname    = "raspberrypi"
address     = "1SNSR"
spi_channel = "MAIN_CE0"
port        = 8888
spi_ce      = 25

RF_Channel = 71
RF_Pa      = RF24_PA.LOW
data_rate  = RF24_DATA_RATE.RATE_1MBPS
crc        = RF24_CRC.BYTES_2

# Create NRF24 object.
# Using main spi with CE0.
# Connect RF_CSN pin to CE0(GPIO8) and connect the RF_CE to ce pin specified below (GPIO25).
nrf = NRF24(pi, ce=spi_ce, spi_channel=spi_channel, channel=RF_Channel ,spi_speed=50e3, pa_level=RF_Pa, data_rate=data_rate, crc_bytes=crc, payload_size=RF24_PAYLOAD.MAX,)
nrf.set_address_bytes(len(address))



def config_SPI_Channel() -> None:
    # Get the channel enumerator.
    spi_channel = SPI_CHANNEL.from_value(spi_channel)

    #Connect to the GPIO daemon.
    print(f'Connecting to GPIO daemon on {hostname}:{port} ...')
    
    pi = pigpio.pi(hostname, port)
    if not pi.connected:
        print("Not connected to Raspberry Pi ... check pigpiod try \"sudo pigpiod\"")
        sys.exit()
    print("Done ...\n")
#end config_SPI_Channel


def send_ack_payload():
    nrf.reset_packages_lost()
    while True:
        nrf.send(payload)
        try:
            nrf.wait_until_sent()
            break
        except TimeoutError:
            print('Timeout, waiting for transmission to complete.')
            # Wait 10 seconds before sending the next reading.
            time.sleep(0.5)
            continue
        #end try
    #end while

    if nrf.get_packages_lost() == 0:
        print(f"Success: lost={nrf.get_packages_lost()}, retries={nrf.get_retries()}")
    else:
        print(f"Error: lost={nrf.get_packages_lost()}, retries={nrf.get_retries()}")
    #end if
#end send_ack_payload()


def hardwareTest() -> None:
    
    #Printing the Values used to initiate the nrf.
    print("\n")
    print("Start Hardware Test ...\n")
    time.sleep(PRINT_DELAY)

    print(f"Initial values:")                         
    print(f"Connection channel: {RF_Channel}, PA level: {RF_Pa.name}")
    print(f"Data rate: {data_rate.name}, CRC: {crc.name}")
    print("\n")
    
    time.sleep(PRINT_DELAY)

    #Start Assertion.
    print("Start asserting ...\n")

    #Asserting the RF Channel
    print("Asserting the RF Channel ...")
    time.sleep(PRINT_DELAY)
    print(f"Channel = {nrf.get_channel()}")
    assert nrf.get_channel() == RF_Channel
    print("Done ...\n")

    #Asserting the PA level
    print("Asserting the PA level ...")
    time.sleep(PRINT_DELAY)
    print(f"PA level= {nrf.get_pa_level().name} ")
    assert nrf.get_pa_level() == RF_Pa
    print("Done ...\n")

    #Asserting the data_rate
    print("Asserting the data_rata ...")
    time.sleep(PRINT_DELAY)
    print(f"data_rate= {nrf.get_data_rate().name}")
    assert nrf.get_data_rate() == data_rate
    print("Done ...\n")

    #Asserting the crc
    print("Asserting the crc ...")
    time.sleep(PRINT_DELAY)
    print(f"CRC Bytes= {nrf.get_crc_bytes().name} ")
    assert nrf.get_crc_bytes()  == crc
    print("Done ...\n")


    print("Test_00 is successfully done.")
#end hardwareTest()
    


#
# A simple NRF24L receiver that connects to a PIGPIO instance on a hostname and port, default "localhost" and 8888, and
# starts receiving data on the address specified.  Use the companion program "simple-sender.py" to send data to it from
# a different Raspberry Pi.
#
if __name__ == "__main__":
   
    config_SPI_Channel()

    # Listen on the address specified as parameter
    nrf.open_reading_pipe(RF24_RX_ADDR.P1, address)
    nrf.open_writing_pipe(address)

    #Set Payload size to 32 byte.
    nrf.set_payload_size(RF24_PAYLOAD.MAX)

    #prepare the ack_payload.
    ack_payload = struct.pack(bytes,RF24NT_HUB_IP, RF24NT_MONITORS_IP, "acknowledged")

    while True:
        if nrf.data_ready():
            now = datetime.now()
            payload:bytes[32] = nrf.get_payload()

            if (payload[0] == RF24NT_MONITORS_IP):
                print("Package Destination IP: {:08b}".format(payload[0]))
                print("Sender IP: {:08b}".format(payload[1]))
                print("Temp: {:.2f}".format(payload[2:5]))
                print("Temp: {:.2f}".format(payload[6:9]))
                print("Location: {:.6f} , {:.6f}".format(payload[10:13], payload[14:17]))
                print("Sensors Bitstream: {:016b}".format(payload[18:21]))

                send_ack_payload()
            #end if
        #end if
    #end while
#end main
            

                

              



