#include "RF24NT.h"


#define RF24NT_PRINT_DELAY 1000 //ms

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


/**********************************************************************/

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


/*********************************************************************************/

RF24NT::RF24NT(uint8_t ce_pin, uint8_t csn_pin):
    RF24(ce_pin ,csn_pin, RF24NT_SPI_SPEED)
{
    //Call the parent's constructor.
}
RF24NT::~RF24NT()
{
    //the parent's destructor will be called automatically.
}


/*****************************************************************************************************************************************/

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

    RF24::enableDynamicPayloads();

    RF24::setRetries(250,1);                        // Leave the retries for the FSM.
    RF24::setPayloadSize(32);                     // Max payload size. 
    
    
    return true;
}



/************************************************************************************/

bool RF24NT::sendPackage(void* data, uint8_t size, uint8_t destination)
{
    rf24nt_payload_t payload;
    payload.destination_IP = destination;
    payload.sender_IP = this->IP;

    uint8_t* data_itr = (uint8_t*)data;
    size = size * sizeof(float);
    uint8_t i = 0;

    while (i < MAX_DATA_SIZE)
    {   
        if (i < size){
            payload.data[i] = *data_itr;
            data_itr += sizeof(uint8_t);
        }
        else {
            payload.data[i] = 0;
        }
        i++;
    }
    
    payload.end_of_transmission = RF24NT_END_OF_TRANSMISSION;

    

    return RF24::write(&payload, MAX_PAYLOAD_SIZE);
}


/*********************************************************************************************************/

bool RF24NT::startHardwareTest(uint8_t rf24nt_rf_channel, uint8_t rf24nt_pa_level, uint8_t rf24nt_data_rate)
{
    Serial.println();
    Serial.println(F("Starting testing the Hardware ..."));
    delay(RF24NT_PRINT_DELAY);

    Serial.println();
    Serial.println(F("Start asserting the registers ..."));
    delay(RF24NT_PRINT_DELAY);

    Serial.println();
    Serial.print(F("Config Reg: ")); Serial.println(this->readConfigReg(), HEX);
    

    Serial.println();
    delay(RF24NT_PRINT_DELAY);

    Serial.println(F("Checking the RF Channel ..."));
    delay(RF24NT_PRINT_DELAY);
    if(this->getChannel() != rf24nt_rf_channel)
    {
        Serial.println(F("Test Failed: RF channel doesn't match the written value."));
        Serial.print(F("RF Channel = ")); Serial.println(this->getChannel());
        return false;
    }
    Serial.println(F("Done ..."));
    delay(RF24NT_PRINT_DELAY);
    Serial.println();


    Serial.println(F("Checking the PA level ...")); 
    delay(RF24NT_PRINT_DELAY);
    if(this->getPALevel() != rf24nt_pa_level)
    {
        Serial.println(F("Test Failed: PA level doesn't match the written value."));
        Serial.print(F("PA level = ")); Serial.println(this->getPALevel_str());
        return false;
    }
    Serial.println(F("Done ..."));
    delay(RF24NT_PRINT_DELAY);
    Serial.println();


    Serial.println(F("Checking the data rate ...")); 
    delay(RF24NT_PRINT_DELAY);
    if(this->getDataRate() != rf24nt_data_rate)
    {
        Serial.println(F("Test Failed: data_rate level doesn't match the written value."));
        Serial.print(F("PA level = ")); Serial.println(this->getDataRate_str());
        return false;
    }
    Serial.println(F("Done ..."));
    Serial.println();
    delay(RF24NT_PRINT_DELAY);

    return true;
}


/**********************************************************************************/
void RF24NT::setID(uint8_t id)
{
    this->ID = id; 
}

void RF24NT::setIP(uint8_t ip)
{
    this->IP = ip;
}

/**********************************************************************************/

void RF24NT::setLocation(float latitude, float longitude)
{
    this->location[0] = (uint32_t)latitude;
    this->location[1] = (uint32_t)longitude;
}

/**********************************************************************************/

void RF24NT::setSensors(uint16_t sensors)
{
    this->sensors = sensors;
}


/**********************************************************************************/

char* RF24NT::getPALevel_str()
{
    return (char*)(pgm_read_ptr(&rf24_pa_dbm_e_str_P[RF24::getPALevel()]));
}


/**********************************************************************************/

char* RF24NT::getDataRate_str()
{
    return (char*)(pgm_read_ptr(&rf24nt_datarate_e_str_P[RF24::getDataRate()]));
}


/*********************************************************************************/

uint8_t RF24NT::readConfigReg()
{
    return read_register(NRF_CONFIG);
}

/*********************************************************************************/

void RF24NT::writeData(rf24nt_payload_t* payload, uint8_t* data, uint8_t size)
{
    for (int i =0; i < size; i++)
    {
        payload->data[i] = data[i];
    }
}

/*********************************************************************************/