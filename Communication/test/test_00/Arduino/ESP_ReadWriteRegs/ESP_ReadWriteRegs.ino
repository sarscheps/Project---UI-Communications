#include <SPI.h>
#include "RF24NT.h"

/*
 * Chip Enable and Chip Select pins.
 * Pins used for the spi communication.
 */
#define CE_PIN   5
#define CSN_PIN  4
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
rf24_pa_dbm_e rf_pa = RF24_PA_LOW;
/*
 * RF24_1MBPS,  RF24_2MBPS, RF24_250KBPS
 * data_rate: Specify the Speed of the communication over the radio.
 * NOTE: Must match with the other devices.
 */
rf24_datarate_e data_rate = RF24_1MBPS;
/*
 * RF24_CRC_DISABLED, RF24_CRC_8, RF24_CRC_16
 * crc_length: Cyclic Redundancy Check length, crc is an error detection mechanism 
 * NOTE: Must match with the other devices.
 */
rf24_crclength_e crc_length = RF24_CRC_16;

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

  Serial.println("Start asserting the registers ...");

  Serial.println("Checking the RF Channel ...");
  if(radio.getChannel() != RF_CHANNEL)
  {
    Serial.println("Test Failed: ");
    Serial.print("RF Channel = "); Serial.println(radio.getChannel());
  }
  Serial.println("Done ...");



  Serial.println("Checking the PA level ...");
  if(radio.getPALevel() != rf_pa)
  {
    Serial.println("Test Failed: ");
    Serial.print("PA level = "); Serial.println(radio.getPALevel_str());
  }
  Serial.println("Done ...");

  while(true);
  //_is_p_variant
 
}

