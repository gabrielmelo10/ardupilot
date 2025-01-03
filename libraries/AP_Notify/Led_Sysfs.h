/*
  Copyright (C) 2017 Emlid Ltd. All rights reserved.

  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/
#pragma once

#include "AP_Notify_config.h"

#if AP_NOTIFY_SYSFS_LED_ENABLED

#include <AP_HAL_Linux/Led_Sysfs.h>

#include "RGBLed.h"

class Led_Sysfs: public RGBLed
{
public:
    Led_Sysfs(const char *red, const char *green, const char *blue,
              uint8_t off_brightness = 0xff , uint8_t low_brightness = 0x00,
              uint8_t medium_brightness = 0x00, uint8_t high_brightness = 0x00);
    bool init(void) override;

protected:
    bool hw_set_rgb(uint8_t r, uint8_t g, uint8_t b) override;

private:
    Linux::Led_Sysfs red_led;
    Linux::Led_Sysfs green_led;
    Linux::Led_Sysfs blue_led;
};
#endif  // AP_NOTIFY_SYSFS_LED_ENABLED
