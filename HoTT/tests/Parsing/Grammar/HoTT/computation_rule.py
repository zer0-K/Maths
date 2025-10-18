###################################################
#                                                 #
#       Tests on computation rules (parsing)      #
#                                                 #
###################################################

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

log_prefix: str = "[Parsing][Grammar][HoTT][computation rule]"


class RUN_COMPUT:

    log_prefix: str = f"{log_prefix}"
    
    @staticmethod
    def run():
        # preprocess
        if True:
            prefix: str = f"{RUN_COMPUT.log_prefix}"

            Logger.test("running...", prefix)
            success: str = "Good"

            test_container = TestContainer()
            # empty context
            test_container.add(
                "let name_p = name_e in (name_e, name_d)", 
                "computation_rule\n" + \
                "  term\tname_p\n" + \
                "  term\tname_e\n" + \
                "  term\n" + \
                "    introduction_rule\n" + \
                "      intro_pair\n" + \
                "        term\tname_e\n" + \
                "        term\tname_d\n")
            
            func: Callable = lambda s: HottParser.get_HoTT_tree(s, "computation_rule").pretty()
        
        # process
        success = UtilsTest.check(func, test_container, log_prefix)
        
        # postprocess
        Logger.test(success, prefix)


class RUN:

    @staticmethod
    def run():
        
        Logger.test("running...", log_prefix)

        RUN_COMPUT.run()
        
        Logger.test("done", log_prefix)


if __name__ == "__main__":
    RUN.run()
