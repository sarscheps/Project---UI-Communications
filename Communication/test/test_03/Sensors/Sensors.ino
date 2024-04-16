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


#define DEVICE_LOCAL_ID          0xE3 
#define NEW_DEVICE_PASSWORD      1234

#define LOC_LATITUDE             2.352654          
#define LOC_LONGITUDE            1.546854

#define THIS_SENSOR_ID           11135
#define AVAILABLE_SENSORS        0x11000000000000000
                                      
// Create NRF24L01 radio.
RF24NT radio(RF24NT_PIN_CE, RF24NT_PIN_CSN);

char ack_str[13] = "acknowledged";

byte rf24nt_tx_address[6] = "1SNSR";    // Address used when transmitting data.
PAYLOAD payload;             // Payload structure. Used both for transmitting and receiving.
SENSOR sensor[10];

uint32_t* uint32_itr;

unsigned long last_reading;                // Milliseconds since last measurement was read.
unsigned long ms_between_reads = 300;    // 10000 ms = 10 seconds
unsigned long ms_timeout_delay = 2000;
unsigned int  ms_sleep_time_ms = 1000;

typedef enum State{INIT, GET_IP, WAIT_FOR_IP, SEND_ACK, SLEEP_MODE, READ_SENSORS, SEND_PACKAGE, WAIT_FOR_ACK} STATE;

STATE state = State::INIT;
bool ip_received = false;
bool timeOut = false;
bool ack_received = false;
uint8_t retries = 0;
uint8_t nextIP = 0;
char* received_str;
byte pipeNum = 0;

float arrayData[6];
uint8_t dataSize = 0;

void getSensorData();

void tickFunc()
{
  // State Transition.
  switch (state)
  {

  case State::INIT:{
    state = State::GET_IP;
    break;
  }

  case State::GET_IP:{
    state = State::WAIT_FOR_IP;
    break;
  }

  case State::WAIT_FOR_IP:{
    if (ip_received){
      state = State::SEND_ACK;
      ip_received = false;
    } else if (timeOut){
      state = State::GET_IP;
      timeOut = false;
    }
    break;
  }
  
  case State::SEND_ACK:{
    state = State::SLEEP_MODE;
    break;
  }

  case State::SLEEP_MODE:{
    state = State::READ_SENSORS;
    break;  
  }

  case State::READ_SENSORS:{
    state = State::SEND_PACKAGE;
    
  }

  case State::SEND_PACKAGE:{
    state = State::WAIT_FOR_ACK;
    timeOut = false;
    break; 
  }

  case State::WAIT_FOR_ACK:{
    if (ack_received)
      state = State::SLEEP_MODE;
    else if (timeOut)
      state = State::SEND_PACKAGE;  
    break;
  }

  default:{

    break;
  }

  } //sWITCH

  // State Action
  switch (state)
  {

  case State::INIT:{
    Serial.println(F("Start the Sensor FSM ..."));
    break;
  }

  case State::GET_IP:{
    arrayData[0] = NEW_DEVICE_PASSWORD;
    arrayData[1] = THIS_SENSOR_ID;
    arrayData[2] = LOC_LATITUDE;
    arrayData[3] = LOC_LONGITUDE;
    arrayData[4] = AVAILABLE_SENSORS;

    radio.setIP(0);
    radio.stopListening();
    if(radio.sendPackage(arrayData, 20, RF24NT_HUB_IP)) {
      Serial.print(F("IP = 0 sent successfully. Retries=")); Serial.println(radio.getARC());
    }
    else {
      Serial.print(F("Failed to send IP = 0. Retries=")); Serial.println(radio.getARC());
      timeOut++;
    } 
    radio.startListening();
    break;
  }

  case State::WAIT_FOR_IP:{
    
    while(millis() - last_reading < ms_timeout_delay)
    {
      if (radio.available(&pipeNum)){
        radio.read(&payload, MAX_PAYLOAD_SIZE);

        uint32_itr = (uint32_t*)payload.data;
        if (uint32_itr != 0){
            ip_received = true;
            radio.setIP((uint8_t)*uint32_itr);
            Serial.print(F("New IP: ")); Serial.println((uint8_t)*uint32_itr, BIN);
            break;
        }
      }
    }

    timeOut = true;
    break;
  }
  
  case State::SEND_ACK:{
    
    for (int i = 0; i < 3; i++)
    {   radio.stopListening();
        if(radio.sendPackage(&ack_str, 13, RF24NT_HUB_IP)) {
            Serial.print(F("Ack sent successfully. Retries=")); Serial.println(radio.getARC());
        }
        else {
            Serial.print(F("Failed to send Ack. Retries=")); Serial.println(radio.getARC());
        }
        radio.startListening();
        delay(500);
    }
    break;
  }


  case State::SLEEP_MODE:{
    //sleep(ms_sleep_time_ms);
    break; 
  } 


  case State::READ_SENSORS:{
    
    
  }


  case State::SEND_PACKAGE:{
    void getSensorData();
    // Send the data ...
    radio.stopListening();
    if (radio.sendPackage(arrayData, dataSize, RF24NT_HUB_IP)) {
      Serial.print(F("Payload sent successfully. Retries=")); Serial.println(radio.getARC());
    }
    else {
      Serial.print(F("Failed to send payload. Retries=")); Serial.println(radio.getARC());
    } 
    radio.startListening();
    // Start listening again.
    break;
  }


  case State::WAIT_FOR_ACK:{
   while(millis() - last_reading < ms_timeout_delay)
    {
      if (radio.available(&pipeNum)){
        radio.read(&payload, MAX_PAYLOAD_SIZE);
        received_str = (char*)payload.data;
        if (strcmp(received_str,"acknowledged") == 0){
          Serial.println("Ack received ...");
          ack_received = true;
          nextIP++;
          break;
        }
      }
    }
    
    retries++;
    timeOut = true;
    break;
  }
  }  
} // tickFunc


void setup() {
  
  // Initialize serial connection.
  Serial.begin(115200);
  while (!Serial) {
    // Waiting for the serial port to be initiated 
  }
  
  // Show that program is starting.
  Serial.println(F("\n\nNRF24L01 Hup FSM."));

  // Configure the NRF24 transceiver.
  Serial.println("Configure NRF24 ...");
  if (!radio.begin(RF24NT_RF_CHANNEL, RF24NT_PA_LEVEL, RF24NT_DATA_RATE, RF24NT_CRC_LENGTH, false))
  {
    Serial.println(F("Error initiating the RF..."));
    Serial.print(F("Check the Spi connection."));
    Serial.print(F("CE --> ")); Serial.println(RF24NT_PIN_CE);
    Serial.print(F("CSN --> ")); Serial.println(RF24NT_PIN_CSN);

  }

  
  /*if (!radio.startHardwareTest(RF24NT_RF_CHANNEL, RF24NT_PA_LEVEL, RF24NT_DATA_RATE))
  {
    while(true);
  }*/
  
  radio.setID(DEVICE_LOCAL_ID);

  radio.openWritingPipe(rf24nt_tx_address);
  radio.openReadingPipe(pipeNum, rf24nt_tx_address);
  radio.startListening();

  last_reading = 0;
}


void loop() {

// Take the current timestamp. This means that the next (first) measurement will be read and
// transmitted in "ms_between_reads" milliseconds.
  if (millis() - last_reading > ms_between_reads) {
    
    // Generate random values for humidity and temperature.
    tickFunc();
    last_reading = millis();
  }
}



void getSensorData(){
    arrayData[0] = random(50, 1100)/10.0;     // Temp
    arrayData[1] = random(10, 100)/100.0;      // Humd
    dataSize = 2;
    
    // Report the temperature and humidity.    
    Serial.print(F("Sensor values: temperature=")); Serial.print(arrayData[0]); 
    Serial.print(F(", humidity=")); Serial.println(arrayData[1]);

}