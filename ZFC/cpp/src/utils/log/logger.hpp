#ifndef MATHS_ZFC_UTILS_LOGGER_H
#define MATHS_ZFC_UTILS_LOGGER_H

#include <iostream>
#include <filesystem>  
#include <fstream>
#include <iomanip>
#include <chrono>
#include <format>
#include <ctime>

namespace fs = std::filesystem;

namespace mzfcutils {
namespace mzfclog {

typedef int int_log_level;

class logger {
private:
    static bool init_log_folder(const fs::path& base_log_folder, const fs::path& log_folder_name);

    static bool init_log_files();

    static bool init_log_file(const std::string& log_file);

    static inline void log(fs::path log_file, const std::string& probes, const std::string& message, const std::string& values);

public:
    static bool enabled;
    static fs::path log_dir;
    static int_log_level log_level;


    static void disable();

    static bool init(const fs::path& base_log_folder, const fs::path& log_folder_name);

    static void set_log_level(int_log_level level);

    static void log_main(const std::string& probes, const std::string& message, const std::string& values, int_log_level level);

    static void log_debug(const std::string& probes, const std::string& message, const std::string& values, int_log_level level);

};

} // mzfcutils
} // mzfclog

#endif