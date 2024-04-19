#include <Arduino.h>
#include <Wire.h>
#include "Adafruit_SHT31.h"

bool enableHeater = false;
uint8_t loopCnt = 0;
bool transmitFlag;
uint32_t transmitTime;

Adafruit_SHT31 sht31 = Adafruit_SHT31();

void setup() {
  Serial.begin(9600);

  if (! sht31.begin(0x44)) {   // Set to 0x45 for alternate I2C address
    Serial.println("Couldn't find SHT31");
    while (1) delay(1);
  }
}

void loop() {
  float t = sht31.readTemperature();
  float h = sht31.readHumidity();

  if (! isnan(t)) {  // check if 'is not a number'
    Serial.print("Temp *C = "); Serial.print(t); Serial.print("\t\t");
  } else { 
    Serial.println("Failed to read temperature");
  }
  
  if (! isnan(h)) {  // check if 'is not a number'
    Serial.print("Hum. % = "); Serial.println(h);
  } else { 
    Serial.println("Failed to read humidity");
  }

  delay(1000);

   // in transmit code need something that sets a flag true when transmitting
  // this is to coordinate the heater to get rid of the condensation in the 
  //sensor
  if(transmitFlag) {
    transmitTime = millis();
    transmitFlag = false;
  }
  
  if(millis() - transmitTime >= (60 * 4750) && millis() - transmitTime <= (60 * 8000)) {
    if (loopCnt >= 60) {
      enableHeater = !enableHeater;
      sht31.heater(enableHeater);
      Serial.print(("Heater Enabled State: "));
      if (sht31.isHeaterEnabled())
        Serial.println(("ENABLED"));
      else
        Serial.println(("DISABLED"));

      loopCnt = 0;
    }
    loopCnt++;
  }
}
