import argparse
import sys

import pigpio
from nrf24 import *
import time


if __name__ == "__main__":
    
    print("Python NRF24 Simple Receiver Example.")
    
    # Parse command line argument.
    parser = argparse.ArgumentParser(prog="simple-receiver.py", description="Simple NRF24 Receiver Example.")
    parser.add_argument('-n', '--hostname', type=str, default='raspberrypi', help="Hostname for the Raspberry running the pigpio daemon.")
    parser.add_argument('-p', '--port', type=int, default=8888, help="Port number of the pigpio daemon.")
    parser.add_argument('address', type=str, nargs='?', default='1SNSR', help="Address to listen to (3 to 5 ASCII characters)")
    parser.add_argument('-s', '--spi', type=str, default="MAIN_CE0", help="Select the Spi Channel, CE0, CE1. Default = MAIN_CE0")
    parser.add_argument('e', '--CE', type=int, default=25, help="RF_CE pin, default GPIO25")

    args        = parser.parse_args()
    hostname    = args.hostname
    port        = args.port
    address     = args.address
    spi_ch      = args.spi
    spi_ce      = args.CE

    RF_Channel = 76
    RF_Pa      = RF24_PA.MIN
    data_rate  = RF24_DATA_RATE.RATE_1MBPS
    crc        = RF24_CRC.BYTES_2 


    # Verify that address is between 3 and 5 characters.
    if not (2 < len(address) < 6):
        print(f'Invalid address {address}. Addresses must be between 3 and 5 ASCII characters.')
        sys.exit(1)

    # Get the channel enumerator.
    spi_ch = SPI_CHANNEL.from_value(spi_ch)
    

    # Connect to pigpio damian using the given port,
    # make sure you run 'sudo pigpiod' before running the test.
    print(f'Connecting to GPIO daemon on {hostname}:{port} ...')
    pi = pigpio.pi(hostname, port)
    if not pi.connected:
        print("Not connected to Raspberry Pi ... check pigpiod")
        sys.exit()


    # Create NRF24 object.
    # Using main spi with CE0.
    # Connect RF_CSN pin to CE0(GPIO8) and connect the RF_CE to ce pin specified below (GPIO25).
    nrf = NRF24(pi, ce=spi_ce, spi_channel=spi_ch, channel=RF_Channel ,spi_speed=50e3, payload_size=RF24_PAYLOAD.MAX,)
    nrf.set_address_bytes(len(address))
    
    if spi_ce < SPI_CHANNEL.AUX_CE0:
        ce_pin = "GPIO8" if (spi_ce == SPI_CHANNEL.MAIN_CE1) else "GPIO7"
    else: 
        ce_pin = "the right GPIO"
    
    # enter s to start the test, q to quit.
    start = input("Start the test?(s/q) make sure the CE pin is connected to {spi_ce}, and the CSN pin is connected to {ce_pin}")
    
    if start:
        while 1:
            try:
                print(
                       "Initial values:                          \n \
                       Connection channel: {RF_Channel}         \n \
                       PA level: {RF_Pa}                        \n \
                       Data rate: {data_rate}                   \n \
                       CRC: {crc}"
                       )
                
                #Start Assertion.
                print("Start asserting ...")

                #Asserting the RF Channel
                print("Assert RF Channel...")
                assert nrf.getChannel()
                time.sleep(0.5)

                
            except:
                None



    # Listen on the address specified as parameter
    #nrf.open_reading_pipe(RF24_RX_ADDR.P1, address)
    
    # Display the content of NRF24L01 device registers.
    #nrf.show_registers()

