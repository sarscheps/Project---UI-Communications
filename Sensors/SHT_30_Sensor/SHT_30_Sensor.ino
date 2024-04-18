#include <Arduino.h>
#include <Wire.h>
#include "Adafruit_SHT31.h"

bool enableHeater = false;
uint8_t loopCnt = 0;
Adafruit_SHT31 sht31 = Adafruit_SHT31();
bool transmitFlag;
unt32_t transmitTime;

void setup() {
  // put your setup code here, to run once:

}

void loop() {
  double t = sht31.readTemperature();
  double h = sht31.readHumidity();

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
      Serial.print("Heater Enabled State: ");
      if (sht31.isHeaterEnabled())
        Serial.println("ENABLED");
      else
        Serial.println("DISABLED");

      loopCnt = 0;
    }
    loopCnt++;
  }
}
