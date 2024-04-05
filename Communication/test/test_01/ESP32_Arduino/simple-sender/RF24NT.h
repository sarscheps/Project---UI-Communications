#ifndef RF24NT_h
#define RF24NT_h

#include <Arduino.h>
#include <SPI.h>

#define MINIMAL     // Disable some functions and variables in RF24 lib that we need to redefine in our library. see line "#if !defined(MINIMAL)" in RF24.cpp 
#include "RF24.h"
#include "nRF24L01.h"

#define RF24NT_SPI_SPEED 50000  //50 Mb

#define RF24NT_SUPPORT_LOCATION
#define RF24NT_SENSOR_DEVICE

#define RF24NT_HUB_IP                   0b10000001
#define RF24NT_MONITORS_IP              0b10000010
#define RF24NT_END_OF_TRANSIMISSION     0b11111111



struct rf24nt_payload_t {     // 32 Bytes Payload.
    uint16_t  package_destination;      // 2 Bytes destination. 
    uint8_t   local_IP;               // 1 Byte IP 
    uint32_t  data[6];          // 28 Bytes data (6 float data); 
    uint8_t   end_of_transmission;              // 1 Byte End of Transmission.

};

typedef rf24nt_payload_t PAYLOAD;

/**
 * @brief 
 * 
 */
class RF24NT: public RF24
{
private:
    uint8_t   IP;                    // Given by the main module.
    uint16_t  ID;                    // unique for each device.

#ifdef RF24NT_SUPPORT_LOCATION
    uint32_t  location[2];           // latitude & longitude
#endif

#ifdef RF24NT_SENSOR_DEVICE 
    uint16_t  sensors;               // Bit string, define the used sensors, eg: first bit for Temp, second bit for Humanity sensor.. etc.
#endif
     
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
                uint8_t rf_channel          = 100,                  // RF_Channel default 100;
                rf24_pa_dbm_e rf_pa         = RF24_PA_MIN,          // 
                rf24_datarate_e data_rate   = RF24_250KBPS,         //
                rf24_crclength_e crc_length = RF24_CRC_DISABLED,    //
                bool auto_ack               = false
                        );

    bool sendPackage(uint32_t* data, uint8_t size);

    /**
     * @brief 
     * 
     */
    bool startHardwareTest(uint8_t rf24nt_rf_channel, uint8_t rf24nt_pa_level, uint8_t rf24nt_data_rate);
    
    /**
     * @brief 
     * 
     * @param ip 
     */
    void setID(uint16_t ip);


#ifdef RF24NT_SUPPORT_LOCATION
    void setLocation(float latitude, float longitude);
#endif

#ifdef RF24NT_SENSOR_DEVICE 
    void setSensors(uint16_t sensors);
#endif
    /**
     * @brief Get the PALevel str object
     * 
     * @return char* 
     */
    char* getPALevel_str();

    /**
     * @brief Get the Data rate str object.
     * 
     * @return char* 
     */
    char* getDataRate_str();

    /**
     * @brief Get Config register.
     * 
     * @return char* 
     */
    uint8_t readConfigReg();

    
};


#endif //RF24NT_H
