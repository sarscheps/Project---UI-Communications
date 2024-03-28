#include <SPI.h>
#include "RF24NT.h"

/*
 * Chip Enable and Chip Select pins.
 * Pins are used for the spi communication.
 */
#define CE_PIN   5
#define CSN_PIN  2
#define IRQ_PIN  0
/*
 * 1 - 100 Mhz 
 * RF_CHANNEL: the commination channel will be 24,000 + RF_CHANNEL MHz
 * NOTE: Must match with the other devices.
 */
#define RF_CHANNEL 71
/*
 * MIN, LOW, HIGH, MAX, ERROR
 * rf_pa: Check the README file for more details.
 * NOTE: Must match with the other devices.
 */
#define rf_pa RF24_PA_LOW
/*
 * RF24_1MBPS,  RF24_2MBPS, RF24_250KBPS
 * data_rate: Specify the Speed of the communication over the radio.
 * NOTE: Must match with the other devices.
 */
#define data_rate RF24_1MBPS
/*
 * RF24_CRC_DISABLED, RF24_CRC_8, RF24_CRC_16
 * crc_length: Cyclic Redundancy Check length, crc is an error detection mechanism 
 * NOTE: Must match with the other devices.
 */
#define crc_length RF24_CRC_16

RF24NT radio(CE_PIN, CSN_PIN);

void setup()
{
  Serial.begin(115200);
  while (!Serial) {
    // Waiting for the serial port to be initiated 
  }
  
}

void loop()
{
  Serial.println();
  Serial.println("Starting Test_00 ...");

  if (radio.begin(RF_CHANNEL, rf_pa, RF24_1MBPS,RF24_CRC_16, false))
  {
    Serial.println("Error initiating the RF...");
    Serial.print("Check the Spi connection.");
    Serial.print("CE --> "); Serial.println(CE_PIN);
    Serial.print("CSN --> "); Serial.println(CSN_PIN);

  }
  Serial.println();
  Serial.println("Start asserting the registers ...");

  Serial.println();
  Serial.print("Config Reg: ");
  Serial.println(radio.readConfigReg(), HEX);
  if (radio.readConfigReg() == 0)
  {
    Serial.println("Test Failed: Check the SPI connection ...");
  } 
  else 
  {
    Serial.println("Test Failed: Cannot write and read from the nRF24L01 module ...");
    Serial.println("Check the Power Supply, or try to replace nRF24L01 module ...");
    Serial.println("If the nRF24L01 module with the antenna is used, make sure to use the regulator module with 5v Power supply ...");
  }
  Serial.println();


  Serial.println("Checking the RF Channel ...");
  radio.setPALevel(RF_CHANNEL);
  if(radio.getChannel() != RF_CHANNEL)
  {
    Serial.println("Test Failed: RF channel doesn't match the writtn value.");
    Serial.print("RF Channel = "); Serial.println(radio.getChannel());
  }
  Serial.println("Done ...");
  Serial.println();


  Serial.println("Checking the PA level ..."); 
  radio.setPALevel(RF24_PA_LOW);
  if(radio.getPALevel() != rf_pa)
  {
    Serial.println("Test Failed: PA level doesn't match the written value.");
    Serial.print("PA level = "); Serial.println(radio.getPALevel_str());
  }
  Serial.println("Done ...");
  Serial.println();


  Serial.println("Checking the data rate ..."); 
  radio.setPALevel(data_rate);
  if(radio.getDataRate() != data_rate)
  {
    Serial.println("Test Failed: data_rate level doesn't match the written value.");
    Serial.print("PA level = "); Serial.println(radio.getDataRate_str());
  }
  Serial.println("Done ...");
  Serial.println();
  

  while(true);
  //_is_p_variant
 
}

