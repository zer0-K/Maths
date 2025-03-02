#ifndef MATHS_ZFC_UTILS_LOGGER_CONSTANTS_H
#define MATHS_ZFC_UTILS_LOGGER_CONSTANTS_H

#include <iostream>

namespace mzfcutils {
namespace mzfclog {

//---------- log files

constexpr inline std::string MAIN_LOG = "main";
constexpr inline std::string DEBUG_LOG = "debug";

//---------- log probes

constexpr inline std::string P_INIT = "[INIT]";

} // mzfcutils
} // mzfclog

#endif