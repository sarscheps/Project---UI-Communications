// RF24, version 1.3.9, by TMRh20
#include "RF24NT.h"

#define RF24NT_PIN_CSN            2             // CSN PIN for RF24 module.
#define RF24NT_PIN_CE             5             // CE PIN for RF24 module.

#define RF24NT_RF_CHANNEL        71             // 0 ... 125
#define RF24NT_CRC_LENGTH         RF24_CRC_16   // RF24_CRC_DISABLED, RF24_CRC_8, RF24_CRC_16 for 16-bit
#define RF24NT_DATA_RATE          RF24_1MBPS    // RF24_2MBPS, RF24_1MBPS, RF24_250KBPS
#define RF24NT_DYNAMIC_PAYLOAD    1
#define RF24NT_PAYLOAD_SIZE      32             // Max. 32 bytes.
#define RF24NT_PA_LEVEL           RF24_PA_LOW   // RF24_PA_MIN, RF24_PA_LOW, RF24_PA_HIGH, RF24_PA_MAX    
#define RF24NT_RETRY_DELAY        5             // Delay bewteen retries, 1..15.  Multiples of 250µs.
#define RF24NT_RETRY_COUNT       15             // Number of retries, 1..15.

#define PROTOCOL 0x01                           // 0x01 (byte), temperature (float), humidity (float)
                                                // Python 1: "<Bff"
                                             
                                      
// Create NRF24L01 radio.
RF24NT radio(RF24NT_PIN_CE, RF24NT_PIN_CSN);

byte rf24nt_tx_address[6] = "1SNSR";    // Address used when transmitting data.
PAYLOAD payload;             // Payload structure. Used both for transmitting and receiving.

unsigned long last_reading;                // Milliseconds since last measurement was read.
unsigned long ms_between_reads = 10000;    // 10000 ms = 10 seconds

void setup() {
  
  // Initialize serial connection.
  Serial.begin(115200);
  while (!Serial) {
    // Waiting for the serial port to be initiated 
  }
  
  // Show that program is starting.
  Serial.println(F("\n\nNRF24L01 Arduino Simple Sender."));

  // Configure the NRF24 tranceiver.
  Serial.println("Configure NRF24 ...");
  if (radio.begin(RF24NT_RF_CHANNEL, RF24NT_PA_LEVEL, RF24NT_DATA_RATE, RF24NT_CRC_LENGTH, false))
  {
    Serial.println(F("Error initiating the RF..."));
    Serial.print(F("Check the Spi connection."));
    Serial.print(F("CE --> ")); Serial.println(RF24NT_PIN_CE);
    Serial.print(F("CSN --> ")); Serial.println(RF24NT_PIN_CSN);

  }

  radio.openWritingPipe(rf24nt_tx_address);
  radio.stopListening();

  // Take the current timestamp. This means that the next (first) measurement will be read and
  // transmitted in "ms_between_reads" milliseconds.
  last_reading = 0;
}

void loop() {

  if (millis() - last_reading > ms_between_reads) {
    // Read sensor values every "ms_between_read" milliseconds.
  
    // Generate random values for humidity and temperature.
    float t, h;
    h = random(50, 1100)/10.0;
    t = random(10, 100)/100.0;
    
    // Report the temperature and humidity.    
    Serial.print(F("Sensor values: temperature=")); Serial.print(t); 
    Serial.print(F(", humidity=")); Serial.println(h);

    // Stop listening on the radio (we can't both listen and send).
    radio.stopListening();

    // Send the data ...
    send_reading(t, h);

    // Start listening again.
    radio.startListening();

    // Register that we have read the temperature and humidity.
    last_reading = millis();
  }
}

void send_reading(float temperature, float humidity)
{
  int offset = 0;

  Serial.print(F("Bytes packed: ")); Serial.println(offset);

  if (radio.write(payload, offset)) {
    Serial.print(F("Payload sent successfully. Retries=")); Serial.println(radio.getARC());
  }
  else {
    Serial.print(F("Failed to send payload. Retries=")); Serial.println(radio.getARC());
  }   
}

void radio_setup()
{
  radio.begin();
  radio.enableDynamicPayloads();

  radio.setRetries(RF24NT_RETRY_DELAY, RF24NT_RETRY_COUNT);
  radio.setPayloadSize(RF24NT_PAYLOAD_SIZE);
    
  radio.stopListening();
}
