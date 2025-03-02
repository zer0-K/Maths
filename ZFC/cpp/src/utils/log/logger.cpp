#include "logger.hpp"

#include "log_probes.hpp"

namespace fs = std::filesystem;

namespace mzfcutils {
namespace mzfclog {

    bool logger::logger::enabled = true;
    int_log_level logger::logger::log_level = 2;
    fs::path logger::logger::log_dir = "/home/adrien/Data/Maths/ZFC";


    bool logger::init_log_folder(const fs::path& base_log_folder, const fs::path& log_folder_name)
    {
        // for ex : project/log
        if(!fs::exists(base_log_folder))
        {
            std::cout << "Folder " << base_log_folder << " does not exist, cannot init logger !" << std::endl;
            return false;
        }

        // for ex : project/log/test1
        fs::path log_folder = base_log_folder / log_folder_name;
        if(!fs::exists(log_folder))
        { 
            fs::create_directory(log_folder);
            std::cout << "Created directory " << log_folder << std::endl;
        }

        // for ex : project/log/test1/2025-03-02_17-20
        auto now = std::chrono::system_clock::now();
        fs::path now_folder = std::format("{:%Y-%m-%d}", now);
        log_folder = log_folder / now_folder;
        if(!fs::exists(log_folder))
        {
            fs::create_directory(log_folder);
            std::cout << "Created directory " << log_folder << std::endl;
        }
        else
        {
            std::cout << "Directory " << log_folder << " already exists" << std::endl;
        }

        logger::log_dir = log_folder;

        return true;
    }


    bool logger::init_log_files()
    {
        bool success = true;

        success = success && init_log_file(mzfclog::MAIN_LOG);
        success = success && init_log_file(mzfclog::DEBUG_LOG);

        return success;
    }


    bool logger::init_log_file(const std::string& log_file)
    {
        fs::path log_file_path_full = logger::log_dir / (log_file + ".log");
        if(fs::exists(log_file_path_full))
        {
            std::cout << "Log file " << log_file_path_full << "already exists" << std::endl; 
        }
        else
        {
            std::ofstream f;
            f.open(log_file_path_full);

            if(!f.is_open()) 
            {
                std::cout << "Error when creating file " << log_file_path_full << std::endl;
                return false;
            }
            std::cout << "File " << log_file_path_full << " created" << std::endl;             
            f.close();
        }

        return true;
    }


    inline void logger::log(fs::path log_file, const std::string& probes, const std::string& message, const std::string& values)
    {
        auto now = std::chrono::high_resolution_clock::now();
        std::string now_str = std::format("{:%Y-%m-%d_%H:%M:%S}", now);
        auto time_since_epoch = now.time_since_epoch();

        std::ofstream f(log_file, std::ios::app);

        f << now_str << "---" << probes << "---" << message << "---" << values << std::endl;

        f.close();
    }


    void logger::disable()
    {
        logger::enabled = false;
    }


    bool logger::init(const fs::path& base_log_folder, const fs::path& log_folder_name)
    {
        if(!logger::enabled) return true;

        std::cout << "Initializing logger..." << std::endl;


        bool success;
        success = init_log_folder(base_log_folder, log_folder_name);
        if(!success)
        {
            std::cout << "Logger not initialized properly when creating logging folders" << std::endl;
            logger::enabled = false;
            return false;
        }
        std::cout << "Log folders initialized" << std::endl;


        success = init_log_files();
        if(!success)
        {
            std::cout << "Logger not initialized properly when creating logging files" << std::endl;
            logger::enabled = false;
            return false;
        }

        logger::log_main(P_INIT, "logger initialized", "", log_level);
        logger::log_debug(P_INIT, "logger initialized", "", log_level);

        std::cout << "Logger initialized. Folders at " << logger::log_dir << ", log level : " << logger::log_level << std::endl;

        return true;
    }


    void logger::set_log_level(int_log_level level)
    {
        if(logger::enabled)
        {
            logger::log_level = level;
            std::cout << "Log level set to " << logger::log_level << std::endl;
        }
    }


    void logger::log_main(const std::string& probes, const std::string& message, const std::string& values, int_log_level level)
    {
        if(logger::enabled && level <= logger::log_level)
        {
            log(logger::log_dir / (mzfclog::MAIN_LOG + ".log"), probes, message, values);
        }
    }


    void logger::log_debug(const std::string& probes, const std::string& message, const std::string& values, int_log_level level)
    {
        if(logger::enabled && level <= logger::log_level)
        {
            log(logger::log_dir / (mzfclog::DEBUG_LOG + ".log"), probes, message, values);
        }
    }

} // mzfcutils
} // mzfclog
