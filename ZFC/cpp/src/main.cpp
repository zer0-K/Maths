#include <iostream>
#include <filesystem>

#include "utils/log/logger.hpp"

namespace fs = std::filesystem;

namespace log = mzfcutils::mzfclog;

int main()
{
    std::cout << "Using c++ "<< __cplusplus << std::endl;

    const fs::path& log_dir = "/home/adrien/Data/Maths/ZFC";
    const fs::path& prefix = "test";
    log::logger::init(log_dir, prefix);

    return 0;
}