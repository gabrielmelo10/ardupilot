/*
 * AP_SBusOut.h
 *
 *  Created on: Aug 19, 2017
 *      Author: Mark Whitehorn
 */

#pragma once

#include "AP_SBusOut_config.h"

#if AP_SBUSOUTPUT_ENABLED

#include <AP_HAL/AP_HAL.h>
#include <AP_Param/AP_Param.h>

class AP_SBusOut {
public:
    AP_SBusOut();

    /* Do not allow copies */
    CLASS_NO_COPY(AP_SBusOut);

    static const struct AP_Param::GroupInfo var_info[];

    void update();

    // public format function for use by IOMCU
    static void sbus_format_frame(uint16_t *channels, uint8_t num_channels, uint8_t buffer[25]);

private:

    AP_HAL::UARTDriver *sbus1_uart;

    void init(void);

    uint16_t sbus_frame_interval;   // microseconds

    AP_Int16 sbus_rate;
    bool initialised;
};

#endif  // AP_SBUSOUTPUT_ENABLED
