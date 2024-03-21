#include "Arduino.h"
#include "SPI.h"
#include "include/printf.h"
#include "include/RF24.h"

/*
 * Chip Enable and Chip Select pins.
 * Pins used for the spi communication.
 */
#define CE_PIN 
#define CSN_PIN 
/*
 * 1 - 100 Mhz 
 * RF_CHANNEL: the commination channel will be 24,000 + RF_CHANNEL MHz
 * NOTE: Must match with the other devices.
 */
#define RF_CHANNEL = 73;
/*
 * HIN, LOW, HIGH, MAX, ERROR
 * rf_pa: Check the README file for more details.
 * NOTE: Must match with the other devices.
 */
rf24_pa_dbm_e rf_pa = RF24_PA_MIN;
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
