/*
  dummy backend barometer. Used during board bringup. Selected using
  BARO line in hwdef.dat
 */
#pragma once

#include "AP_Baro_Backend.h"

#if AP_BARO_DUMMY_ENABLED

class AP_Baro_Dummy : public AP_Baro_Backend
{
public:
    AP_Baro_Dummy(AP_Baro &baro);
    void update(void) override;
    static AP_Baro_Backend *probe(AP_Baro &baro) {
        return NEW_NOTHROW AP_Baro_Dummy(baro);
    }

private:
    uint8_t _instance;
};

#endif  // AP_BARO_DUMMY_ENABLED
