// RF24, version 1.3.9, by TMRh20
#include "src/RF24NT.h"
#include <Wire.h>
#include "Adafruit_SHT31.h"


#define RF24NT_PIN_CSN            5             // CSN PIN for RF24 module.
#define RF24NT_PIN_CE             4             // CE PIN for RF24 module.

#define RF24NT_RF_CHANNEL        71             // 0 ... 125
#define RF24NT_CRC_LENGTH         RF24_CRC_16   // RF24_CRC_DISABLED, RF24_CRC_8, RF24_CRC_16 for 16-bit
#define RF24NT_DATA_RATE          RF24_1MBPS    // RF24_2MBPS, RF24_1MBPS, RF24_250KBPS
#define RF24NT_DYNAMIC_PAYLOAD    1
#define RF24NT_PAYLOAD_SIZE      32             // Max. 32 bytes.
#define RF24NT_PA_LEVEL           RF24_PA_LOW   // RF24_PA_MIN, RF24_PA_LOW, RF24_PA_HIGH, RF24_PA_MAX    
#define RF24NT_RETRY_DELAY        5             // Delay bewteen retries, 1..15.  Multiples of 250µs.
#define RF24NT_RETRY_COUNT       15             // Number of retries, 1..15.

#define RF24NT_HUB_IP            0b10000000
#define RF24NT_MONITORS_IP       0b10000001   

#define DEVICE_LOCAL_ID          0xE3

//Sensor Variables
bool enableHeater = false;
uint8_t loopCnt = 0;
Adafruit_SHT31 sht31 = Adafruit_SHT31();
bool transmitFlag = false;
uint32_t transmitTime = 0;
                                      
// Create NRF24L01 radio.
RF24NT radio(RF24NT_PIN_CE, RF24NT_PIN_CSN);

byte rf24nt_tx_address[6] = "1SNSR";    // Address used when transmitting data.
PAYLOAD payload;             // Payload structure. Used both for transmitting and receiving.

unsigned long last_reading;                // Milliseconds since last measurement was read.
unsigned long sec_between_reads = 6;    // 10000 ms = 10 seconds

void setup() {
  
  // Initialize serial connection.
  Serial.begin(115200);

  if (! sht31.begin(0x44)) {   // Set to 0x45 for alternate I2C address
  Serial.println("Couldn't find SHT31");
  while (1) delay(1);
  }
  
  while (!Serial) {
    // Waiting for the serial port to be initiated 
  }
  
  // Show that program is starting.
  Serial.println(F("\n\nNRF24L01 Arduino Simple Sender."));

  // Configure the NRF24 transceiver.
  Serial.println("Configure NRF24 ...");
  if (!radio.begin(RF24NT_RF_CHANNEL, RF24NT_PA_LEVEL, RF24NT_DATA_RATE, RF24NT_CRC_LENGTH, false))
  {
    Serial.println(F("Error initiating the RF..."));
    Serial.print(F("Check the Spi connection."));
    Serial.print(F("CE --> ")); Serial.println(RF24NT_PIN_CE);
    Serial.print(F("CSN --> ")); Serial.println(RF24NT_PIN_CSN);
  }

  radio.setID(DEVICE_LOCAL_ID);

  radio.openWritingPipe(rf24nt_tx_address);
  //radio.openReadingPipe(0, rf24nt_tx_address);
  
  // Take the current timestamp. This means that the next (first) measurement will be read and
  // transmitted in "sec_between_reads" milliseconds.
  /*if (!radio.startHardwareTest(RF24NT_RF_CHANNEL, RF24NT_PA_LEVEL, RF24NT_DATA_RATE))
  {
    while(true);
  }*/
  last_reading = 0;
}


void loop() {

    Serial.print("Milli-last_reading: ");
    Serial.println(millis() - last_reading);

  if ((millis() - last_reading) / 1000 > sec_between_reads) {
    
    float t = sht31.readTemperature();
    float h = sht31.readHumidity();

    // Generate random values for humidity and temperature.
    float data[2];
    data[0] = sht31.readTemperature();     // Temp
    data[1] = sht31.readHumidity();      // Humd
    
    // Report the temperature and humidity.    
    if (! isnan(t)) {  // check if 'is not a number'
      Serial.print("Temp *C = "); 
      Serial.print(t); 
      Serial.print("\t\t");
    } 
    else { 
      Serial.println("Failed to read temperature");
    }
  
    if (! isnan(h)) {  // check if 'is not a number'
      Serial.print("Hum. % = "); 
      Serial.println(h);
    } 
    else { 
      Serial.println("Failed to read humidity");
    }

    

    // Stop listening on the radio (we can't both listen and send).
    radio.stopListening();

    // Send the data ...
    if (radio.sendPackage(data, 2, RF24NT_HUB_IP)) {
      Serial.print(F("Payload sent successfully. Retries=")); Serial.println(radio.getARC());
      transmitFlag = true;
      transmitTime = millis();
    }
    else {
      Serial.print(F("Failed to send payload. Retries=")); Serial.println(radio.getARC());
    } 
    // Start listening again.
    radio.startListening();

    // Register that we have read the temperature and humidity.
    last_reading = millis();   
  }
  else {
    if(transmitFlag) {
      if(loopCnt >= (sec_between_reads / 2)) {
        sht31.heater(true);
        Serial.println("Heating");
        if (loopCnt >= 1) {
          sht31.heater(false);
          transmitFlag = false;
          loopCnt = 0;
        }
        
      } 
      Serial.print("Milli-Transmit: ");
      Serial.println(millis()-transmitTime);
    }
  }
  loopCnt++;
  delay(1000);
}
