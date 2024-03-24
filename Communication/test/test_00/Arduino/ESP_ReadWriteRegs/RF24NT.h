#ifndef RF24NT_h
#define RF24NT_h

#include <SPI.h>
#include "RF24.h"

#define RF24NT_SPI_SPEED 50000  //50 Mb

class RF24NT: public RF24
{
private:
    /* data */
public:
    RF24NT(u_int8_t ce_pin, u_int8_t csn_pin);
    ~RF24NT();

    bool begin( 
                u_int8_t rf_channel = 100, 
                rf24_pa_dbm_e rf_pa = RF24_PA_MIN, 
                rf24_datarate_e data_rate = RF24_250KBPS, 
                rf24_crclength_e crc_length = RF24_CRC_DISABLED, 
                bool auto_ack = false
                        );
    
    inline char* getPALevel();
};


#endif //RF24NT_H