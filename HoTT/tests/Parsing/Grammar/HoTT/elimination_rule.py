##############################################
#                                            #
#       Tests on eliminations (parsing)      #
#                                            #
##############################################

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
from src.Parsing.Grammar.hott_parser import Parser

log_prefix: str = "[Parsing][Grammar][HoTT][elimination]"


class RUN_INTRO:

    log_prefix: str = f"{log_prefix}[simple]"
    
    @staticmethod
    def unit():
        # preprocess
        if True:
            prefix: str = f"{RUN_INTRO.log_prefix}"

            Logger.test("running...", prefix)
            success: str = "Good"

            test_container = TestContainer()
            test_container.add("absurd Type", "elim_empty\n  term\n    universe\n")
            
            # starting point in the grammar is the node 'universe'
            func: Callable = lambda s: Parser.get_HoTT_tree(s, "elim_empty").pretty()
        
        # process
        success = UtilsTest.check(func, test_container, log_prefix)
        
        # postprocess
        Logger.test(success, prefix)


class RUN:

    @staticmethod
    def run():
        
        Logger.test("running...", log_prefix)

        RUN_INTRO.unit()
        
        Logger.test("done", log_prefix)


if __name__ == "__main__":
    RUN.run()

