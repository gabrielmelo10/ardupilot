#pragma once

#include "RCInput.h"
#include <AP_HAL/utility/Socket_native.h>
#include "RCInput_UDP_Protocol.h"

#define RCINPUT_UDP_DEF_PORT 777

namespace Linux {

class RCInput_UDP : public RCInput
{
public:
    RCInput_UDP();
    void init() override;
    void _timer_tick(void) override;
private:
    SocketAPM_native _socket{true};
    uint16_t     _port;
    struct rc_udp_packet_v3 _buf;
    uint64_t _last_buf_ts;
    uint16_t _last_buf_seq;
};

}
