#include "RF24NT.h"

RF24NT::RF24NT(u_int8_t ce_pin, u_int8_t csn_pin):
    RF24(ce_pin ,csn_pin, RF24NT_SPI_SPEED)
{
    //Call the parent's constructor.
}
RF24NT::~RF24NT()
{
    //the parent's destructor will be called automatically.
}


bool RF24NT::begin(u_int8_t rf_channel, rf24_pa_dbm_e rf_pa, rf24_datarate_e data_rate, rf24_crclength_e crc_length, bool auto_ack)
{

    if(!(RF24::begin()))
    {
        return false;
    }
    
    RF24::setPALevel(rf_pa);
    RF24::setDataRate(data_rate);
    RF24::setChannel(rf_channel);
    RF24::setCRCLength(crc_length);
    RF24::setAutoAck(auto_ack);
    
    return true;
}

inline char* RF24NT::getPALevel()
{
    uint8_t value = RF24::getPALevel();
    switch (value)
    { // MIN, LOW, HIGH, MAX, ERROR 
    case 0:
        return "MIN";
    case 1:
        return ("RF24_PA_LOW");
    case 2:
        return "HIGH";
    case 3:
        return "MAX";
    default:
        return "ERROR";
    }
}
