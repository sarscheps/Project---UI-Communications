#ifndef RF24NT_h
#define RF24NT_h

#include <Arduino.h>
#include <SPI.h>

//#define MINIMAL     // Disable some functions and variables in RF24 lib that we need to redefine in our library. see line "#if !defined(MINIMAL)" in RF24.cpp 
#include "RF24.h"




#define RF24NT_SPI_SPEED 50000  //50 Mb

class RF24NT: public RF24
{
private:
    /* data */
public:
    RF24NT(uint8_t ce_pin, uint8_t csn_pin);
    ~RF24NT();
    
    char* getPALevel_str();
    bool begin( 
                uint8_t rf_channel         = 100, 
                rf24_pa_dbm_e rf_pa         = RF24_PA_MIN, 
                rf24_datarate_e data_rate   = RF24_250KBPS, 
                rf24_crclength_e crc_length = RF24_CRC_DISABLED, 
                bool auto_ack               = false
                        );
};


#endif //RF24NT_H
