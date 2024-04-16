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

#define RF24NT_HUB_IP                   0b10000001
#define RF24NT_MONITORS_IP              0b10000010
                                     
// Create NRF24L01 radio.
RF24NT radio(RF24NT_PIN_CE, RF24NT_PIN_CSN);

byte    rf24nt_tx_address[6] = "1SNSR";          // Address used when transmitting data.
PAYLOAD payload;                              // Payload structure. Used both for transmitting and receiving.

unsigned long last_reading;                   // Milliseconds since last measurement was read.
unsigned long ms_between_reads = 300;        // 200 ms = 0.2 seconds


void setup() {
  // Initialize serial connection.
  Serial.begin(115200);
  while (!Serial) {
    // Waiting for the serial port to be initiated 
  }
  
  // Show that program is starting.
  Serial.println(F("\n\nNRF24L01 Arduino Simple Reciver."));

  // Configure the NRF24 tranceiver.
  Serial.println("Configure NRF24 ...");
  if (!radio.begin(RF24NT_RF_CHANNEL, RF24NT_PA_LEVEL, RF24NT_DATA_RATE, RF24NT_CRC_LENGTH, false))
  {
    Serial.println(F("Error initiating the RF..."));
    Serial.print(F("Check the Spi connection."));
    Serial.print(F("CE --> ")); Serial.println(RF24NT_PIN_CE);
    Serial.print(F("CSN --> ")); Serial.println(RF24NT_PIN_CSN);

  }

  if (!radio.startHardwareTest(RF24NT_RF_CHANNEL, RF24NT_PA_LEVEL, RF24NT_DATA_RATE))
  {
    while(true);
  }

  radio.openReadingPipe(0, rf24nt_tx_address);
  radio.startListening();
  // Take the current timestamp. This means that the next (first) measurement will be read and
  // transmitted in "ms_between_reads" milliseconds.
  last_reading = 0;
}


void loop() {

  if (millis() - last_reading > ms_between_reads) {
    byte pipNum = 0;
    // Send the data ...
    if (radio.available(&pipNum)) {
      Serial.println("Strat Reciving ...");
      
      radio.read(&payload, MAX_PAYLOAD_SIZE);

      Serial.print(F("Received payload from IP: ")); Serial.println(payload.destination_IP, BIN);
      Serial.print(F("Sender IP: ")); Serial.println(payload.local_IP,BIN);
      
      float* itr = (float*)payload.data;
      
      Serial.print(F("Temp: ")); Serial.println(*itr);
      Serial.print(F("Humidity: ")); Serial.println(*(++itr));


    } else {
      Serial.println("Nothing Received ...");
    }

    // Register that we have read the temperature and humidity.
    last_reading = millis();
  }
}


