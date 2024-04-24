import argparse
from datetime import datetime
import struct
import sys
import time
import traceback
import os
import csv

import pigpio
from nrf24 import *



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

curr_dir = os.path.dirname(__file__)


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


#
# A simple NRF24L receiver that connects to a PIGPIO instance on a hostname and port, default "localhost" and 8888, and
# starts receiving data on the address specified.  Use the companion program "simple-sender.py" to send data to it from
# a different Raspberry Pi.
#
if __name__ == "__main__":


    # Verify that address is between 3 and 5 characters.
    if not (2 < len(address) < 6):
        print(f'Invalid address {address}. Addresses must be between 3 and 5 ASCII characters.')
        sys.exit(1)
    
    # Connect to pigpiod
    print(f'Connecting to GPIO daemon on {hostname}:{port} ...')
    pi = pigpio.pi(hostname, port)
    if not pi.connected:
        print("Not connected to Raspberry Pi ... goodbye.")
        sys.exit()

    # Create NRF24 object.
    # Using main spi with CE0.
    # Connect RF_CSN pin to CE0(GPIO8) and connect the RF_CE to ce pin specified below (GPIO25).
    nrf = NRF24(pi, ce=spi_ce, spi_channel=spi_channel, channel=RF_Channel ,spi_speed=50e3, pa_level=RF_Pa, data_rate=data_rate, crc_bytes=crc, payload_size=RF24_PAYLOAD.MAX,)
    nrf.set_address_bytes(len(address))

    # Listen on the address specified as parameter
    nrf.open_reading_pipe(RF24_RX_ADDR.P1, address)
    
    # Display the content of NRF24L01 device registers.
    hardwareTest()

    # Enter a loop receiving data on the address specified.
    try:
        print(f'Receive from {address}')
        while True:

            # As long as data is ready for processing, process it.
            while nrf.data_ready():
                current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                
                # Read pipe and payload for message.
                pipe = nrf.data_pipe()
                payload:bytes[32] = nrf.get_payload()    

                print("Package Destination IP: {:08b}".format(payload[0]))
                print("Sender IP: {:08b}".format(payload[1]))
                print("Temp: {:.2f}".format(payload[2:5]))
                print("Temp: {:.2f}".format(payload[6:9]))

                with open(os.path.join(curr_dir, "data_src/test_received_data.csv"),'w', newline='') as csvFile:
                    writer = csv.writer(csvFile)
                    # Write the data to the CSV file
                    writer.writerow([current_time, "{:.2f}".format(payload[0]), "{:.2f}".format(payload[1])])


                csvFile.close()

                time.sleep(0.25)
    except:
        traceback.print_exc()
        nrf.power_down()
        pi.stop()
