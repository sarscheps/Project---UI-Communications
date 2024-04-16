// RF24, version 1.3.9, by TMRh20
#include "src/RF24NT.h"

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
                                      
// Create NRF24L01 radio.
RF24NT radio(RF24NT_PIN_CE, RF24NT_PIN_CSN);

byte rf24nt_tx_address[6] = "1SNSR";    // Address used when transmitting data.
PAYLOAD payload;             // Payload structure. Used both for transmitting and receiving.

unsigned long last_reading;                // Milliseconds since last measurement was read.
unsigned long ms_between_reads = 6000;    // 10000 ms = 10 seconds

void setup() {
  
  // Initialize serial connection.
  Serial.begin(115200);
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
  // transmitted in "ms_between_reads" milliseconds.
  /*if (!radio.startHardwareTest(RF24NT_RF_CHANNEL, RF24NT_PA_LEVEL, RF24NT_DATA_RATE))
  {
    while(true);
  }*/
  last_reading = 0;
}


void loop() {

  if (millis() - last_reading > ms_between_reads) {
    
    // Generate random values for humidity and temperature.
    float data[2];
    data[0] = random(50, 1100)/10.0;     // Temp
    data[1] = random(10, 100)/100.0;      // Humd
    
    // Report the temperature and humidity.    
    Serial.print(F("Sensor values: temperature=")); Serial.print(data[0]); 
    Serial.print(F(", humidity=")); Serial.println(data[1]);

    // Stop listening on the radio (we can't both listen and send).
    radio.stopListening();

    // Send the data ...
    if (radio.sendPackage(data, 2, RF24NT_HUB_IP)) {
      Serial.print(F("Payload sent successfully. Retries=")); Serial.println(radio.getARC());
    }
    else {
      Serial.print(F("Failed to send payload. Retries=")); Serial.println(radio.getARC());
    } 
    // Start listening again.
    radio.startListening();

    // Register that we have read the temperature and humidity.
    last_reading = millis();
    
  }
}
