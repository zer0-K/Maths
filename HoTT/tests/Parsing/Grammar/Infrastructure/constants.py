#########################################################
#                                                       #
#       Tests on the constants of the HoTT grammar      #
#                                                       #
#########################################################

import sys
import traceback
from typing import Dict
from collections.abc import Callable

proj_dir = "Maths/HoTT".lower()
hott_dir = __file__[:__file__.lower().rfind(proj_dir) + len(proj_dir)]
if hott_dir not in sys.path:
    sys.path = [hott_dir] + sys.path

from src.Utils.logging import Logger
from src.Utils.utils_test import TestContainer, UtilsTest
from src.Parsing.Grammar.hott_parser import get_HoTT_tree

log_prefix: str = "[Parsing][Grammar][Infra][constants]"


class RUN_NUMBER:

    log_prefix: str = f"{log_prefix}[numbers]"
    
    @staticmethod
    def allowed():
        # preprocess
        if True:
            prefix: str = f"{RUN_NUMBER.log_prefix}[allowed numbers]"

            Logger.test("running...", prefix)
            success: str = "Good"

            test_container = TestContainer()
            test_container.add("0", "")
            
            func: Callable = lambda s: get_HoTT_tree(s).pretty()
        
        # process
        success = UtilsTest.check(func, test_container, log_prefix)
        
        # postprocess
        Logger.test(success, prefix)
        

class RUN:

    @staticmethod
    def run():
        
        Logger.test("running...", log_prefix)

        RUN_NUMBER.allowed()
        
        Logger.test("done", log_prefix)

if __name__ == "__main__":
    RUN.run()
