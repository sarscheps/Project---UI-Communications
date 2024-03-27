#ifndef RF24NT_h
#define RF24NT_h

#include <Arduino.h>
#include <SPI.h>

#define MINIMAL     // Disable some functions and variables in RF24 lib that we need to redefine in our library. see line "#if !defined(MINIMAL)" in RF24.cpp 
#include "RF24.h"
#include "nRF24L01.h"

#define RF24NT_SPI_SPEED 50000  //50 Mb

/**
 * @brief 
 * 
 */
class RF24NT: public RF24
{
private:
    /* data */
public:
    /**
     * @brief Construct a new RF24NT object
     * 
     * @param ce_pin 
     * @param csn_pin 
     */
    RF24NT(uint8_t ce_pin, uint8_t csn_pin);

    /**
     * @brief Destroy the RF24NT object
     * 
     */
    ~RF24NT();
    
    /**
     * @brief Get the PALevel str object
     * 
     * @return char* 
     */
    char* getPALevel_str();
    uint8_t readConfigReg();

    /**
     * @brief 
     * 
     * @param rf_channel 
     * @param rf_pa 
     * @param data_rate 
     * @param crc_length 
     * @param auto_ack 
     * @return true 
     * @return false 
     */
    bool begin( 
                uint8_t rf_channel         = 100, 
                rf24_pa_dbm_e rf_pa         = RF24_PA_MIN, 
                rf24_datarate_e data_rate   = RF24_250KBPS, 
                rf24_crclength_e crc_length = RF24_CRC_DISABLED, 
                bool auto_ack               = false
                        );
};


#endif //RF24NT_H
