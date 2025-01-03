#include <AP_WheelEncoder/AP_WheelRateControl.h>

extern const AP_HAL::HAL& hal;

const AP_Param::GroupInfo AP_WheelRateControl::var_info[] = {
    // @Param: _ENABLE
    // @DisplayName: Wheel rate control enable/disable
    // @Description: Enable or disable wheel rate control
    // @Values: 0:Disabled,1:Enabled
    // @User: Standard
    AP_GROUPINFO_FLAGS("_ENABLE", 1, AP_WheelRateControl, _enabled, 0, AP_PARAM_FLAG_ENABLE),

    // @Param: _RATE_MAX
    // @DisplayName: Wheel max rotation rate
    // @Description: Wheel max rotation rate
    // @Units: rad/s
    // @Range: 0 200
    // @User: Standard
    AP_GROUPINFO("_RATE_MAX", 2, AP_WheelRateControl, _rate_max, AP_WHEEL_RATE_MAX_DEFAULT),

    // @Param: _RATE_FF
    // @DisplayName: Wheel rate control feed forward gain
    // @Description: Wheel rate control feed forward gain.  Desired rate (in radians/sec) is multiplied by this constant and output to output (in the range -1 to +1)
    // @Range: 0.100 2.000
    // @User: Standard

    // @Param: _RATE_P
    // @DisplayName: Wheel rate control P gain
    // @Description: Wheel rate control P gain.  Converts rate error (in radians/sec) to output (in the range -1 to +1)
    // @Range: 0.100 2.000
    // @User: Standard

    // @Param: _RATE_I
    // @DisplayName: Wheel rate control I gain
    // @Description: Wheel rate control I gain.  Corrects long term error between the desired rate (in rad/s) and actual
    // @Range: 0.000 2.000
    // @User: Standard

    // @Param: _RATE_IMAX
    // @DisplayName: Wheel rate control I gain maximum
    // @Description: Wheel rate control I gain maximum.  Constrains the output (range -1 to +1) that the I term will generate
    // @Range: 0.000 1.000
    // @User: Standard

    // @Param: _RATE_D
    // @DisplayName: Wheel rate control D gain
    // @Description: Wheel rate control D gain.  Compensates for short-term change in desired rate vs actual
    // @Range: 0.000 0.400
    // @User: Standard

    // @Param: _RATE_FILT
    // @DisplayName: Wheel rate control filter frequency
    // @Description: Wheel rate control input filter.  Lower values reduce noise but add delay.
    // @Range: 1.000 100.000
    // @Units: Hz
    // @User: Standard

    // @Param: _RATE_FLTT
    // @DisplayName: Wheel rate control target frequency in Hz
    // @Description: Wheel rate control target frequency in Hz
    // @Range: 1 50
    // @Increment: 1
    // @Units: Hz
    // @User: Standard

    // @Param: _RATE_FLTE
    // @DisplayName: Wheel rate control error frequency in Hz
    // @Description: Wheel rate control error frequency in Hz
    // @Range: 1 50
    // @Increment: 1
    // @Units: Hz
    // @User: Standard

    // @Param: _RATE_FLTD
    // @DisplayName: Wheel rate control derivative frequency in Hz
    // @Description: Wheel rate control derivative frequency in Hz
    // @Range: 1 50
    // @Increment: 1
    // @Units: Hz
    // @User: Standard

    // @Param: _RATE_SMAX
    // @DisplayName: Wheel rate slew rate limit
    // @Description: Sets an upper limit on the slew rate produced by the combined P and D gains. If the amplitude of the control action produced by the rate feedback exceeds this value, then the D+P gain is reduced to respect the limit. This limits the amplitude of high frequency oscillations caused by an excessive gain. The limit should be set to no more than 25% of the actuators maximum slew rate to allow for load effects. Note: The gain will not be reduced to less than 10% of the nominal value. A value of zero will disable this feature.
    // @Range: 0 200
    // @Increment: 0.5
    // @User: Advanced

    // @Param: _RATE_PDMX
    // @DisplayName: Wheel rate control PD sum maximum
    // @Description: Wheel rate control PD sum maximum.  The maximum/minimum value that the sum of the P and D term can output
    // @Range: 0.000 1.000

    // @Param: _RATE_D_FF
    // @DisplayName: Wheel rate Derivative FeedForward Gain
    // @Description: FF D Gain which produces an output that is proportional to the rate of change of the error
    // @Range: 0.000 0.400
    // @Increment: 0.001
    // @User: Advanced

    // @Param: _RATE_NTF
    // @DisplayName: Wheel rate Target notch filter index
    // @Description: Wheel rate Target notch filter index
    // @Range: 1 8
    // @User: Advanced

    // @Param: _RATE_NEF
    // @DisplayName: Wheel rate Error notch filter index
    // @Description: Wheel rate Error notch filter index
    // @Range: 1 8
    // @User: Advanced

    AP_SUBGROUPINFO(_rate_pid0, "_RATE_", 3, AP_WheelRateControl, AC_PID),

    // @Param: 2_RATE_FF
    // @DisplayName: Wheel rate control feed forward gain
    // @Description: Wheel rate control feed forward gain.  Desired rate (in radians/sec) is multiplied by this constant and output to output (in the range -1 to +1)
    // @Range: 0.100 2.000
    // @User: Standard

    // @Param: 2_RATE_P
    // @DisplayName: Wheel rate control P gain
    // @Description: Wheel rate control P gain.  Converts rate error (in radians/sec) to output (in the range -1 to +1)
    // @Range: 0.100 2.000
    // @User: Standard

    // @Param: 2_RATE_I
    // @DisplayName: Wheel rate control I gain
    // @Description: Wheel rate control I gain.  Corrects long term error between the desired rate (in rad/s) and actual
    // @Range: 0.000 2.000
    // @User: Standard

    // @Param: 2_RATE_IMAX
    // @DisplayName: Wheel rate control I gain maximum
    // @Description: Wheel rate control I gain maximum.  Constrains the output (range -1 to +1) that the I term will generate
    // @Range: 0.000 1.000
    // @User: Standard

    // @Param: 2_RATE_D
    // @DisplayName: Wheel rate control D gain
    // @Description: Wheel rate control D gain.  Compensates for short-term change in desired rate vs actual
    // @Range: 0.000 0.400
    // @User: Standard

    // @Param: 2_RATE_FILT
    // @DisplayName: Wheel rate control filter frequency
    // @Description: Wheel rate control input filter.  Lower values reduce noise but add delay.
    // @Range: 1.000 100.000
    // @Units: Hz
    // @User: Standard

    // @Param: 2_RATE_FLTT
    // @DisplayName: Wheel rate control target frequency in Hz
    // @Description: Wheel rate control target frequency in Hz
    // @Range: 1 50
    // @Increment: 1
    // @Units: Hz
    // @User: Standard

    // @Param: 2_RATE_FLTE
    // @DisplayName: Wheel rate control error frequency in Hz
    // @Description: Wheel rate control error frequency in Hz
    // @Range: 1 50
    // @Increment: 1
    // @Units: Hz
    // @User: Standard

    // @Param: 2_RATE_FLTD
    // @DisplayName: Wheel rate control derivative frequency in Hz
    // @Description: Wheel rate control derivative frequency in Hz
    // @Range: 1 50
    // @Increment: 1
    // @Units: Hz
    // @User: Standard

    // @Param: 2_RATE_SMAX
    // @DisplayName: Wheel rate slew rate limit
    // @Description: Sets an upper limit on the slew rate produced by the combined P and D gains. If the amplitude of the control action produced by the rate feedback exceeds this value, then the D+P gain is reduced to respect the limit. This limits the amplitude of high frequency oscillations caused by an excessive gain. The limit should be set to no more than 25% of the actuators maximum slew rate to allow for load effects. Note: The gain will not be reduced to less than 10% of the nominal value. A value of zero will disable this feature.
    // @Range: 0 200
    // @Increment: 0.5
    // @User: Advanced

    // @Param: 2_RATE_PDMX
    // @DisplayName: Wheel rate control PD sum maximum
    // @Description: Wheel rate control PD sum maximum.  The maximum/minimum value that the sum of the P and D term can output
    // @Range: 0.000 1.000

    // @Param: 2_RATE_D_FF
    // @DisplayName: Wheel rate Derivative FeedForward Gain
    // @Description: FF D Gain which produces an output that is proportional to the rate of change of the target
    // @Range: 0.000 0.400
    // @Increment: 0.001
    // @User: Advanced

    // @Param: 2_RATE_NTF
    // @DisplayName: Wheel rate Target notch filter index
    // @Description: Wheel rate Target notch filter index
    // @Range: 1 8
    // @User: Advanced

    // @Param: 2_RATE_NEF
    // @DisplayName: Wheel rate Error notch filter index
    // @Description: Wheel rate Error notch filter index
    // @Range: 1 8
    // @User: Advanced

    AP_SUBGROUPINFO(_rate_pid1, "2_RATE_", 4, AP_WheelRateControl, AC_PID),

    AP_GROUPEND
};

AP_WheelRateControl::AP_WheelRateControl(const AP_WheelEncoder &wheel_encoder_ref) :
        _wheel_encoder(wheel_encoder_ref)
{
    AP_Param::setup_object_defaults(this, var_info);
}

// returns true if a wheel encoder and rate control PID are available for this instance
bool AP_WheelRateControl::enabled(uint8_t instance)
{
    // sanity check instance
    if ((instance > 1) || (_enabled == 0)) {
        return false;
    }
    // wheel encoder enabled
    return _wheel_encoder.enabled(instance);
}

// get throttle output in the range -100 to +100 given a desired rate expressed as a percentage of the rate_max (-100 to +100)
// instance can be 0 or 1
float AP_WheelRateControl::get_rate_controlled_throttle(uint8_t instance, float desired_rate_pct, float dt)
{
    if (!enabled(instance)) {
        return 0;
    }

    // determine which PID instance to use
    AC_PID& rate_pid = (instance == 0) ? _rate_pid0 : _rate_pid1;

    // check for timeout
    uint32_t now = AP_HAL::millis();
    if (now - _last_update_ms > AP_WHEEL_RATE_CONTROL_TIMEOUT_MS) {
        rate_pid.reset_filter();
        rate_pid.reset_I();
        _limit[instance].lower = false;
        _limit[instance].upper = false;
    }
    _last_update_ms = now;

    // convert desired rate as a percentage to radians/sec
    float desired_rate = desired_rate_pct * 0.01f * get_rate_max_rads();

    // get actual rate from wheel encoder
    float actual_rate = _wheel_encoder.get_rate(instance);

    // constrain and set limit flags
    float output = rate_pid.update_all(desired_rate, actual_rate, dt, (_limit[instance].lower || _limit[instance].upper));
    output += rate_pid.get_ff();

    // set limits for next iteration
    _limit[instance].upper = output >= 100.0f;
    _limit[instance].lower = output <= -100.0f;

    return output;
}

// get pid objects for reporting
AC_PID& AP_WheelRateControl::get_pid(uint8_t instance)
{
    if (instance == 0) {
        return _rate_pid0;
    } else {
        return _rate_pid1;
    }
}

void AP_WheelRateControl::set_notch_sample_rate(float sample_rate)
{
#if AP_FILTER_ENABLED
    _rate_pid0.set_notch_sample_rate(sample_rate);
    _rate_pid1.set_notch_sample_rate(sample_rate);
#endif
}
