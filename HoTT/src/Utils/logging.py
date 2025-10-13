################################
#                              #
#       Logging utilities      #
#                              #
################################

DEFAULT_LOG_LEVEL: int = 10


class Logger:
    """Logger : 
    set Logger.enabled to False if you want to disable the logger
    set Logger.raise_error to True if you want to stop the program instead of just printing the error
    Logger.log_level is a way not to show 'useless' messages (0 : important, 1000: not important)
    """

    enabled: bool = True
    raise_error: bool = False
    log_level: int = DEFAULT_LOG_LEVEL
    
    @staticmethod
    def info(text: str, log_prefix: str = "", log_level: int = DEFAULT_LOG_LEVEL):
        Logger._log(f"Info  : {text}", log_level)
             
    @staticmethod
    def warn(text: str, log_prefix: str = "", log_level: int = DEFAULT_LOG_LEVEL):
        Logger._log(f"Warn  : {text}", log_level)
             
    @staticmethod
    def error(text: str, log_prefix: str = "", log_level: int = DEFAULT_LOG_LEVEL):
        Logger._log(f"Error : {text}", log_level)
        if Logger.raise_error:
            raise Exception(f"{log_prefix} {text}")
             
    @staticmethod
    def debug(text: str, log_prefix: str = "", log_level: int = DEFAULT_LOG_LEVEL):
        Logger._log(f"Debug : {text}", log_level)
             
    @staticmethod
    def test(text: str, log_prefix: str = "", log_level: int = DEFAULT_LOG_LEVEL):
        Logger._log(f"Test  : {text}", log_level)
             
    @staticmethod
    def _log(text: str, log_prefix: str = "", log_level: int = DEFAULT_LOG_LEVEL):
        if Logger.enabled and Logger.log_level >= log_level:
            print(f"{log_prefix} {text}")
