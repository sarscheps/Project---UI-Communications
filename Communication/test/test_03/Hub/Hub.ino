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
#define NEW_DEVICE_PASSWORD      1234

#define MAX_IP_NUMBER            32


                                      
// Create NRF24L01 radio.
RF24NT radio(RF24NT_PIN_CE, RF24NT_PIN_CSN);

char ack_str[13] = "acknowledged";

byte rf24nt_tx_address[6] = "1SNSR";    // Address used when transmitting data.
PAYLOAD payload;             // Payload structure. Used both for transmitting and receiving.
SENSOR sensor[10];

float* float_itr;
uint32_t* uint32_itr;

unsigned long last_reading;                // Milliseconds since last measurement was read.
unsigned long ms_between_reads = 100;    // 10000 ms = 10 seconds
unsigned long ms_timeout_delay = 2000;

typedef enum State{INIT, LISTENING_MODE, READ_PAYLOAD, CHECK_PASSWORD, ASSIGN_IP, WAIT_FOR_IP_ACK, SEND_ACK, SEND_TO_MONITORS, WAIT_FOR_ACK} STATE;

STATE state = State::INIT;
bool correctPassword = false;
bool timeOut = false;
bool ack_received = false;
bool its_ack_payload = false;
uint8_t retries = 0;
uint8_t nextIP = 0;           // MAX = 32
char* received_str;
byte pipeNum = 0;
uint32_t arrayData[6];




void tickFunc()
{
  // State Transition.
  switch (state)
  {

  case State::INIT:
  {
    state = State::LISTENING_MODE;
    break;
  }

  case State::LISTENING_MODE:{
    if (radio.available(&pipeNum))
      state = State::READ_PAYLOAD;
    break;
  }

  case State::READ_PAYLOAD:{
    if ((payload.destination_IP != RF24NT_HUB_IP) || its_ack_payload) {
      state = State::LISTENING_MODE;
    } else if(payload.sender_IP == 0){
      state = State::CHECK_PASSWORD;
      correctPassword = false;
    }
    else{
      state = State::SEND_ACK;
    }
    break;
  }
  
  case State::SEND_ACK:{
    state = State::SEND_TO_MONITORS;
    retries = 0;
    break;
  }

  case State::SEND_TO_MONITORS:{
    if (retries > 3){
      state = State::LISTENING_MODE;
      retries = 0;
    }
    else {
      state = State::WAIT_FOR_ACK;
      timeOut = false;
      ack_received = false;
    }
    break;  
  }

  case State::WAIT_FOR_ACK:{
    if (ack_received){
      state = State::LISTENING_MODE;
      ack_received = false;
    }
    else if (timeOut){
      state = State::ASSIGN_IP;
      timeOut = false;
    }
    break;
  }

  case State::CHECK_PASSWORD:{
    if (correctPassword)
    {
      state = State::ASSIGN_IP;
      correctPassword = false;
      retries = 0;
    }
    else
    {
      state = State::LISTENING_MODE;
    }break; 
  }

  case State::ASSIGN_IP:{
    if (retries > 3){
      state = State::LISTENING_MODE;
      retries = 0;
    }
    else {
      state = State::WAIT_FOR_IP_ACK;
      timeOut = false;
      ack_received = false;
    }
    break;
  }

  case State::WAIT_FOR_IP_ACK:{
    if (ack_received){
      state = State::LISTENING_MODE;
      ack_received = false;
    }
    else if (timeOut){
      state = State::ASSIGN_IP;
      timeOut = false;
    }
    break;
  

  default:
    break;
  }

  } //sWITCH

  // State Action
  switch (state)
  {

  case State::INIT:{
    Serial.println(F("Start the Hub FSM ..."));
    break;
  }

  case State::LISTENING_MODE:{
    Serial.println(F("Nothing received ..."));
    break;
  }

  case State::READ_PAYLOAD:{
    
    radio.read(&payload, MAX_PAYLOAD_SIZE);
    received_str = (char*)payload.data;
    if (strcmp(received_str,  ack_str) == 0){
      its_ack_payload = true;
      Serial.println("Ack Payload ...");
      break;
    } else{
      
      Serial.print(F("Package Destination IP: ")); Serial.println(payload.destination_IP, BIN);
      Serial.print(F("Sender IP: ")); Serial.println(payload.sender_IP,BIN);
      
      float_itr = (float*)payload.data;

      if (payload.sender_IP == 0){
        Serial.print(F("Latitude: ")); Serial.println(*(++float_itr));  
        Serial.print(F("Longitude: ")); Serial.println(*(++float_itr));
        Serial.print(F("Sensors Bits: ")); Serial.println((uint32_t)(*(++float_itr)), BIN);
      } else {
        Serial.print(F("Temp: ")); Serial.println(*float_itr);
        Serial.print(F("Humidity: ")); Serial.println(*(++float_itr));
      }
    }
    break;
  }
  
  case State::SEND_ACK:{
    radio.stopListening();
    for (int i = 0; i < 3; i++){
      if(radio.sendPackage(&ack_str, 13, payload.sender_IP)) {
        Serial.print(F("Ack sent successfully. Retries=")); Serial.println(radio.getARC());
      }
      else {
        Serial.print(F("Failed to send Ack. Retries=")); Serial.println(radio.getARC());
      } 
    }
    radio.startListening();
    break;
  }


  case State::SEND_TO_MONITORS:{
    //Should have a list of Monitor IPs
    float_itr = (float*)payload.data;
    
    arrayData[0] = *float_itr;        //Temp
    arrayData[1] = *(++float_itr);    //Hum
    arrayData[2] = sensor[nextIP].latitude;
    arrayData[3] = sensor[nextIP].longitude;
    arrayData[4] = sensor[nextIP].sensors;
    
    radio.stopListening();
    if(radio.sendPackage(arrayData, 20, RF24NT_MONITORS_IP)) {
      Serial.print(F("Data sent to monitors successfully. Retries=")); Serial.println(radio.getARC());
    }
    else {
      Serial.print(F("Failed to send data to monitors. Retries=")); Serial.println(radio.getARC());
      timeOut++;
    } 
    radio.startListening();
    break; 
  } 


  case State::WAIT_FOR_ACK:{
    while(millis() - last_reading < ms_timeout_delay)
    {
      if (radio.available(&pipeNum)){
        radio.read(&payload, MAX_PAYLOAD_SIZE);
        if (payload.sender_IP == RF24NT_MONITORS_IP){
          received_str = (char*)payload.data;
          if (strcmp(received_str,"acknowledged") == 0){
            Serial.println("Monitor Ack Received ...");
            ack_received = true;
            break;
          }
        }
      }
    }
  
    retries++;
    ack_received = true; // FIX ME: delete this when monitor is used
    timeOut = true;
    break;
  }


  case State::CHECK_PASSWORD:{
    float_itr = (float*)payload.data;
    correctPassword = (*float_itr == NEW_DEVICE_PASSWORD);
    break;
  }


  case State::ASSIGN_IP:{

    if (nextIP >= MAX_IP_NUMBER)
      break;
    uint32_itr = (uint32_t*)payload.data;

    sensor[nextIP].IP = nextIP | 0b10100000;          // IP always start with 101
    sensor[nextIP].ID = *(++uint32_itr);             //uint32_itr is the Password.
    sensor[nextIP].latitude = *(++uint32_itr);
    sensor[nextIP].longitude = *(++uint32_itr);
    sensor[nextIP].sensors = *(++uint32_itr);       // Bit string, define the used sensors, eg: first bit for Temp, second bit for Humanity sensor.. etc.
    
    radio.stopListening();
    if(radio.sendPackage(&sensor[nextIP].IP, 4, payload.sender_IP)) {
      Serial.print(F("IP sent successfully. Retries=")); Serial.println(radio.getARC());
    }
    else {
      Serial.print(F("Failed to send IP. Retries=")); Serial.println(radio.getARC());
      timeOut++;
    } 
    radio.startListening();
    break;
  }

  case State::WAIT_FOR_IP_ACK:{
    while(millis() - last_reading < ms_timeout_delay)
    {
      if (radio.available(&pipeNum)){
        radio.read(&payload, MAX_PAYLOAD_SIZE);
        received_str = (char*)payload.data;
        if (strcmp(received_str,"acknowledged") == 0){
          Serial.println("IP Successfully assigned ...");
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

  } // switch
  
  
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

  
  if (!radio.startHardwareTest(RF24NT_RF_CHANNEL, RF24NT_PA_LEVEL, RF24NT_DATA_RATE))
  {
    while(true);
  }
  
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
