#include <SPI.h>
#include "RF24NT.h"

/*
 * Chip Enable and Chip Select pins.
 * Pins are used for the spi communication.
 */
#define RF24NT_PIN_CE   5
#define RF24NT_PIN_CSN  4
#define RF24NT_PIN_IRQ  0
/*
 * 1 - 100 Mhz 
 * RF_CHANNEL: the commination channel will be 24,000 + RF_CHANNEL MHz
 * NOTE: Must match with the other devices.
 */
#define RF24NT_RF_CHANNEL 71
/*
 * MIN, LOW, HIGH, MAX, ERROR
 * rf_pa: Check the README file for more details.
 * NOTE: Must match with the other devices.
 */
#define RF24NT_PA_LEVEL RF24_PA_LOW
/*
 * RF24_1MBPS,  RF24_2MBPS, RF24_250KBPS
 * data_rate: Specify the Speed of the communication over the radio.
 * NOTE: Must match with the other devices.
 */
#define RF24NT_DATA_RATE RF24_1MBPS
/*
 * RF24_CRC_DISABLED, RF24_CRC_8, RF24_CRC_16
 * crc_length: Cyclic Redundancy Check length, crc is an error detection mechanism 
 * NOTE: Must match with the other devices.
 */
#define RF24NT_CRC_LENGTH RF24_CRC_16

RF24NT radio(RF24NT_PIN_CE, RF24NT_PIN_CSN);

void setup()
{
  Serial.begin(115200);
  while (!Serial) {
    // Waiting for the serial port to be initiated 
  }
  
   if (radio.begin(RF24NT_RF_CHANNEL, RF24NT_PA_LEVEL, RF24NT_DATA_RATE, RF24NT_CRC_LENGTH, false))
  {
    Serial.println(F("Error initiating the RF..."));
    Serial.print(F("Check the Spi connection."));
    Serial.print(F("CE --> ")); Serial.println(RF24NT_PIN_CE);
    Serial.print(F("CSN --> ")); Serial.println(RF24NT_PIN_CSN);

  }
}

void loop()
{
  Serial.println();
  Serial.println(F("Starting Test_00 ..."));
\
  Serial.println();
  Serial.println(F("Start asserting the registers ..."));

  Serial.println();
  Serial.print(F("Config Reg: "));
  Serial.println(radio.readConfigReg(), HEX);

  if (radio.readConfigReg() == 0)
  {
    Serial.println(F("Test Failed: Check the SPI connection ..."));
  } 
  else 
  {
    Serial.println(F("Test Failed: Cannot write and read from the nRF24L01 module ..."));
    Serial.println(F("Check the Power Supply, or try to replace nRF24L01 module ..."));
    Serial.println(F("If the nRF24L01 module with the antenna is used, make sure to use the regulator module with 5v Power supply ..."));
  }
  Serial.println();


  Serial.println(F("Checking the RF Channel ..."));
  if(radio.getChannel() != RF24NT_RF_CHANNEL)
  {
    Serial.println(F("Test Failed: RF channel doesn't match the written value."));
    Serial.print(F("RF Channel = ")); Serial.println(radio.getChannel());
  }
  Serial.println(F("Done ..."));
  Serial.println();


  Serial.println(F("Checking the PA level ...")); 
  if(radio.getPALevel() != RF24NT_PA_LEVEL)
  {
    Serial.println(F("Test Failed: PA level doesn't match the written value."));
    Serial.print(F("PA level = ")); Serial.println(radio.getPALevel_str());
  }
  Serial.println(F("Done ..."));
  Serial.println();


  Serial.println(F("Checking the data rate ...")); 
  if(radio.getDataRate() != RF24NT_DATA_RATE)
  {
    Serial.println(F("Test Failed: data_rate level doesn't match the written value."));
    Serial.print(F("PA level = ")); Serial.println(radio.getDataRate_str());
  }
  Serial.println(F("Done ..."));
  Serial.println();
  

  while(true);
  //_is_p_variant
 
}

