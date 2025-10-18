#######################################
#                                     #
#       Tests on terms (parsing)      #
#                                     #
#######################################

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
from src.Parsing.Grammar.hott_parser import HottParser

log_prefix: str = "[Parsing][Grammar][HoTT][term]"


class RUN_TERM:

    log_prefix: str = f"{log_prefix}[simple]"
    
    @staticmethod
    def run():
        # preprocess
        if True:
            prefix: str = f"{RUN_TERM.log_prefix}"

            Logger.test("running...", prefix)
            success: str = "Good"

            test_container = TestContainer()
            test_container.add("Type_010", "term\n  universe\t010\n")
            test_container.add("var_test_1", "term\n  var\tvar_test_1\n")
            test_container.add("star", "term\tstar\n")
            
            func: Callable = lambda s: HottParser.get_HoTT_tree(s, "term").pretty()
        
        # process
        success = UtilsTest.check(func, test_container, log_prefix)
        
        # postprocess
        Logger.test(success, prefix)


class RUN:

    @staticmethod
    def run():
        
        Logger.test("running...", log_prefix)

        RUN_TERM.run()
        
        Logger.test("done", log_prefix)


if __name__ == "__main__":
    RUN.run()
