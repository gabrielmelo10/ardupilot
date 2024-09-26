#pragma once

#include <AP_HAL/AP_HAL_Boards.h>

#include <AP_Filesystem/AP_Filesystem_config.h>

#ifndef AP_PARAM_DEFAULTS_FILE_PARSING_ENABLED
#define AP_PARAM_DEFAULTS_FILE_PARSING_ENABLED AP_FILESYSTEM_FILE_READING_ENABLED
#endif

#ifndef FORCE_APJ_DEFAULT_PARAMETERS
#define FORCE_APJ_DEFAULT_PARAMETERS 0
#endif
