#include <SPI.h>
#include "src/RF24NT.h"

/*
 * Chip Enable and Chip Select pins.
 * Pins are used for the spi communication.
 */
#define RF24NT_PIN_CE   4
#define RF24NT_PIN_CSN  5
#define RF24NT_PIN_IRQ  22
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
  
   if (!radio.begin(RF24NT_RF_CHANNEL, RF24NT_PA_LEVEL, RF24NT_DATA_RATE, RF24NT_CRC_LENGTH, false))
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

  Serial.println();
  Serial.println(F("Start asserting the registers ..."));

  if (!radio.startHardwareTest(RF24NT_RF_CHANNEL, RF24NT_PA_LEVEL, RF24NT_DATA_RATE))
  {
    while(true);
  }
  Serial.println("Test Done ...");
  while(true);
}
