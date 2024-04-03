// RF24, version 1.3.9, by TMRh20
#include "printf.h"
#include "RF24.h"


#define PIN_RF24_CSN            7            // CSN PIN for RF24 module.
#define PIN_RF24_CE             8            // CE PIN for RF24 module.

#define NRF24_CHANNEL          100            // 0 ... 125
#define NRF24_CRC_LENGTH         RF24_CRC_16  // RF24_CRC_DISABLED, RF24_CRC_8, RF24_CRC_16 for 16-bit
#define NRF24_DATA_RATE          RF24_250KBPS // RF24_2MBPS, RF24_1MBPS, RF24_250KBPS
#define NRF24_DYNAMIC_PAYLOAD    1
#define NRF24_PAYLOAD_SIZE      32            // Max. 32 bytes.
#define NRF24_PA_LEVEL           RF24_PA_MIN  // RF24_PA_MIN, RF24_PA_LOW, RF24_PA_HIGH, RF24_PA_MAX    
#define NRF24_RETRY_DELAY        5            // Delay bewteen retries, 1..15.  Multiples of 250µs.
#define NRF24_RETRY_COUNT       15            // Number of retries, 1..15.

#define PROTOCOL 0x01                         // 0x01 (byte), temperature (float), humidity (float)
                                              // Python 1: "<Bff"
                                             
                                      
// Cretate NRF24L01 radio.
RF24 radio(PIN_RF24_CE, PIN_RF24_CSN);

byte rf24_tx[6] = "1SNSR";    // Address used when transmitting data.
//byte address[] [6] = {"pipe1", "pipe2"};//set addresses of the 2 pipes for read and write

byte payload[32];             // Payload bytes. Used both for transmitting and receiving

unsigned long last_reading;                // Milliseconds since last measurement was read.
unsigned long ms_between_reads = 10000;    // 10000 ms = 10 seconds

boolean buttonState = false;//used for both transmission and receive

void setup() {
  
  // Initialize serial connection.
  Serial.begin(115200);
  printf_begin();
  delay(100);
  
  // Show that program is starting.
  Serial.println("\n\nNRF24L01 Arduino Simple Receiver.");

  // Configure the NRF24 tranceiver.
  Serial.println("Configure NRF24 ...");
  nrf24_setup();
  Serial.println("Configuration Done ...");
  
  // Show debug information for NRF24 tranceiver.
  radio.printDetails();

  // Take the current timestamp. This means that the next (first) measurement will be read and
  // transmitted in "ms_between_reads" milliseconds.
  last_reading = 0;
}

void loop() {
  int offset = 0; 
  //Receive button change from the other Arduino
    delay(100);
    radio.startListening();
    if (radio.available())//do we have transmission from other Arduino board
    {
      Serial.print("Message Received: \n");
      radio.read(payload, offset);//update the variable with new state
      float t, h;
      memcpy(payload + offset, (byte *)(&protocol), sizeof(protocol)); offset += sizeof(protocol); 
      memcpy(payload + offset, (byte *)(&temperature), sizeof(temperature)); offset += sizeof(temperature);
      memcpy(payload + offset, (byte *)(&humidity), sizeof(humidity)); offset += sizeof(humidity);
      radio.stopListening();
    }
}

void nrf24_setup()
{
  radio.begin();
  radio.enableDynamicPayloads();
  radio.setAutoAck(true);               
  radio.setPALevel(NRF24_PA_LEVEL);
  radio.setRetries(NRF24_RETRY_DELAY, NRF24_RETRY_COUNT);              
  radio.setDataRate(NRF24_DATA_RATE);          
  radio.setChannel(NRF24_CHANNEL);
  radio.setCRCLength(NRF24_CRC_LENGTH);
  radio.setPayloadSize(NRF24_PAYLOAD_SIZE);
  //radio.openWritingPipe(rf24_tx);  
  radio.openReadingPipe(rf24_tx,rf24_tx);//open reading pipe from address pipe 2
  radio.stopListening();
}

