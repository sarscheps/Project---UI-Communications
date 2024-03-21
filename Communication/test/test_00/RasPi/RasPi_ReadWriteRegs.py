import argparse
import sys

import pigpio
from nrf24 import *
import time


if __name__ == "__main__":
    
    print("Python NRF24 Hardware Connection test.")
    
    # Parse command line argument.
    parser = argparse.ArgumentParser(prog="simple-receiver.py", description="Simple NRF24 Receiver Example.")
    parser.add_argument('-n', '--hostname', type=str, default='raspberrypi', help="Hostname for the Raspberry running the pigpio daemon.")
    parser.add_argument('-p', '--port', type=int, default=8888, help="Port number of the pigpio daemon.")
    parser.add_argument('address', type=str, nargs='?', default='1SNSR', help="Address to listen to (3 to 5 ASCII characters)")
    parser.add_argument('-s', '--spi', type=str, default="MAIN_CE0", help="Select the Spi Channel, CE0, CE1. Default = MAIN_CE0")
    parser.add_argument('-e', '--CE', type=int, default=25, help="RF_CE pin, default GPIO25")

    args        = parser.parse_args()
    hostname    = args.hostname
    port        = args.port
    address     = args.address
    spi_channel = args.spi
    spi_ce      = args.CE

    RF_Channel = 76
    RF_Pa      = RF24_PA.MIN
    data_rate  = RF24_DATA_RATE.RATE_1MBPS
    crc        = RF24_CRC.BYTES_1 


    # Verify that address is between 3 and 5 characters.
    if not (2 < len(address) < 6):
        print(f'Invalid address {address}. Addresses must be between 3 and 5 ASCII characters.')
        sys.exit(1)

    # Get the channel enumerator.
    spi_channel = SPI_CHANNEL.from_value(spi_channel)


    # Connect to pigpio damian using the given port,
    # make sure you run 'sudo pigpiod' before running the test.
    print(f'Connecting to GPIO daemon on {hostname}:{port} ...')
    pi = pigpio.pi(hostname, port)
    if not pi.connected:
        print("Not connected to Raspberry Pi ... check pigpiod try \"sudo pigpiod\"")
        sys.exit()
    print("Done ...\n")


    # Create NRF24 object.
    # Using main spi with CE0.
    # Connect RF_CSN pin to CE0(GPIO8) and connect the RF_CE to ce pin specified below (GPIO25).
    nrf = NRF24(pi, ce=spi_ce, spi_channel=spi_channel, channel=RF_Channel ,spi_speed=50e3,pa_level=RF_Pa, data_rate=data_rate, crc_bytes=crc, payload_size=RF24_PAYLOAD.MAX,)
    nrf.set_address_bytes(len(address))
    

    # Find the CSN pin according to the spi channel.
    if spi_channel < SPI_CHANNEL.AUX_CE0:
        spi_csn = "GPIO8" if spi_channel == SPI_CHANNEL.MAIN_CE0 else "GPIO7"
    else: 
        spi_csn = "the right GPIO"
    
    # enter y to start the test, q to quit.
    input_str = f"Start the test?(y/q) make sure the CE pin is connected to {spi_ce}, And the CSN pin is connected to {spi_csn}: "
    
    while True:
        try:
            start_test = input(input_str)
            if (start_test not in ['y', 'Y', "yes"]):
                sys.exit()
                
            #Printing the Values used to initiate the nrf.
            print("\n")
            print(f"Initial values:")                         
            print(f"Connection channel: {RF_Channel}, PA level: {RF_Pa.name}")
            print(f"Data rate: {data_rate.name}, CRC: {crc.name}")
            print("\n")
            
            time.sleep(3)

            #Start Assertion.
            print("Start asserting ...\n")

            #Asserting the RF Channel
            print("Asserting the RF Channel ...")
            time.sleep(3)
            print(f"Channel = {nrf.get_channel()}")
            assert nrf.get_channel() == RF_Channel
            print("Done ...\n")

            #Asserting the PA level
            print("Asserting the PA level ...")
            time.sleep(3)
            print(f"PA level= {nrf.get_pa_level().name} ")
            assert nrf.get_pa_level() == RF_Pa
            print("Done ...\n")

            #Asserting the data_rate
            print("Asserting the data_rata ...")
            time.sleep(3)
            print(f"data_rate= {nrf.get_data_rate().name}")
            assert nrf.get_data_rate() == data_rate
            print("Done ...\n")

            #Asserting the crc
            print("Asserting the crc ...")
            time.sleep(3)
            print(f"CRC Bytes= {nrf.get_crc_bytes().name} ")
            assert nrf.get_crc_bytes()  == crc
            print("Done ...\n")
       

            print("Test_00 is successfully done.")
            sys.exit()
            
        except AssertionError:
            # Fail to read one of the registers, 
            print("Fail test_00: Consult the README file on how to connect the nRF24 to the RasPi \n")
            input_str = f"Restart the test?:"
            continue
        



