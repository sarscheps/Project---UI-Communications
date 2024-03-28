#include "RF24NT.h"


static const PROGMEM char rf24nt_datarate_e_str_0[] = "= 1 MBPS";
static const PROGMEM char rf24nt_datarate_e_str_1[] = "= 2 MBPS";
static const PROGMEM char rf24nt_datarate_e_str_2[] = "= 250 KBPS";

static const PROGMEM char rf24nt_model_e_str_0[] = "nRF24L01";
static const PROGMEM char rf24nt_model_e_str_1[] = "nRF24L01+";

static const PROGMEM char rf24nt_crclength_e_str_0[] = "= Disabled";
static const PROGMEM char rf24nt_crclength_e_str_1[] = "= 8 bits";
static const PROGMEM char rf24nt_crclength_e_str_2[] = "= 16 bits";

static const PROGMEM char rf24nt_pa_dbm_e_str_0[] = "= PA_MIN";
static const PROGMEM char rf24nt_pa_dbm_e_str_1[] = "= PA_LOW";
static const PROGMEM char rf24nt_pa_dbm_e_str_2[] = "= PA_HIGH";
static const PROGMEM char rf24nt_pa_dbm_e_str_3[] = "= PA_MAX";
static const PROGMEM char rf24nt_pa_dbm_e_str_4[] = "= PA_ERROR";

static const PROGMEM char rf24nt_feature_e_str_on[]       = "= Enabled";
static const PROGMEM char rf24nt_feature_e_str_allowed[]  = "= Allowed";
static const PROGMEM char rf24nt_feature_e_str_open[]     = " open ";
static const PROGMEM char rf24nt_feature_e_str_closed[]   = "closed";



static const PROGMEM char* const rf24nt_datarate_e_str_P[] = {
    rf24nt_datarate_e_str_0,
    rf24nt_datarate_e_str_1,
    rf24nt_datarate_e_str_2,
};

static const PROGMEM char* const rf24_model_e_str_P[] = {
    rf24nt_model_e_str_0,
    rf24nt_model_e_str_1,
};

static const PROGMEM char* const rf24_crclength_e_str_P[] = {
    rf24nt_crclength_e_str_0,
    rf24nt_crclength_e_str_1,
    rf24nt_crclength_e_str_2,
};

static const PROGMEM char* const rf24_pa_dbm_e_str_P[] = {
    rf24nt_pa_dbm_e_str_0,
    rf24nt_pa_dbm_e_str_1,
    rf24nt_pa_dbm_e_str_2,
    rf24nt_pa_dbm_e_str_3,
    rf24nt_pa_dbm_e_str_4,
};


static const PROGMEM char* const rf24_feature_e_str_P[] = {
    rf24nt_crclength_e_str_0,
    rf24nt_feature_e_str_on,
    rf24nt_feature_e_str_allowed,
    rf24nt_feature_e_str_closed,
    rf24nt_feature_e_str_open,
};



RF24NT::RF24NT(uint8_t ce_pin, uint8_t csn_pin):
    RF24(ce_pin ,csn_pin, RF24NT_SPI_SPEED)
{
    //Call the parent's constructor.
}
RF24NT::~RF24NT()
{
    //the parent's destructor will be called automatically.
}


bool RF24NT::begin(uint8_t rf_channel, rf24_pa_dbm_e rf_pa, rf24_datarate_e data_rate, rf24_crclength_e crc_length, bool auto_ack)
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

char* RF24NT::getPALevel_str()
{
    return (char*)(pgm_read_ptr(&rf24_pa_dbm_e_str_P[RF24::getPALevel()]));
}

char* RF24NT::getDataRate_str()
{
    return (char*)(pgm_read_ptr(&rf24nt_datarate_e_str_P[RF24::getDataRate()]));
}

uint8_t RF24NT::readConfigReg()
{
    return read_register(NRF_CONFIG);
}

