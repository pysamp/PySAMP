#pragma once
#define PY_TEST (0)
#define PY_TRACE (1)

//#define SAMPGDK_MIN_LOG_LEVEL 0

#include <stdio.h>
#include <string.h>
#include <thread>

#include "logging/logger.h"
#include "config.h"
#include "sampgdk.h"
#include "pysamp/pysamp.h"
#include "test/callbackstest.h"
