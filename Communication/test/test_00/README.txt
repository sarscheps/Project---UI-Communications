Testing the Hardware and the SPI connection.

The file ReadWriteRegs.py use the selected spi channel to write some configurations 
values to the nRF2L01 registers and read them back to make sure the comuncation and 
the nRF2L01 chips are working.

If asserting the crc bytes return "DISABLED", make sure the used nrf24.py file is one 
included in this repository or fix the bug in function "get_crc_bytes(self)".