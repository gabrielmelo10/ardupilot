/*
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

#include "AP_ADSB_Backend.h"

#if HAL_ADSB_ENABLED

/*
  base class constructor.
*/
AP_ADSB_Backend::AP_ADSB_Backend(AP_ADSB &frontend, uint8_t instance) :
    _instance(instance),
    _frontend(frontend)
{
}

#endif // HAL_ADSB_ENABLED

