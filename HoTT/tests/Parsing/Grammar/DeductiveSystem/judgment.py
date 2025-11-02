##########################################
#                                        #
#       Tests on judgments (parsing)      #
#                                        #
##########################################

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

log_prefix: str = "[Parsing][Grammar][Logic][judgment]"


class RUN_JUDGMENT:

    log_prefix: str = f"{log_prefix}"
    
    @staticmethod
    def run():
        # preprocess
        if True:
            prefix: str = f"{RUN_JUDGMENT.log_prefix}"

            Logger.test("running...", prefix)
            success: str = "Good"

            test_container = TestContainer()
            # valid context
            test_container.add("empty_context ctx", "judgment\n  context\tempty_context\n")
            # reduction
            test_container.add("empty_context ⊢ Type_1 reduc Type", 
                               "judgment\n" + \
                               "  context\tempty_context\n" + \
                               "  term\n" + \
                               "    universe\t1\n" + \
                               "  term\n" + \
                               "    universe\n")
            # typing
            test_container.add("empty_context ⊢ Type : Type_1", 
                               "judgment\n" + \
                                "  context\tempty_context\n" + \
                                "  term\n" + \
                                "    universe\n" + \
                                "  term\n" + \
                                "    universe\t1\n")
            # definitional equality 
            test_container.add("empty_context ⊢ Type \equiv Type : Type_1", 
                               "judgment\n" + \
                               "  context\tempty_context\n" + \
                               "  term\n" + \
                               "    universe\n" + \
                               "  term\n" + \
                               "    universe\n" + \
                               "  term\n" + \
                               "    universe\t1\n")
            
            func: Callable = lambda s: HottParser.get_HoTT_tree(s, "judgment").pretty()
        
        # process
        success = UtilsTest.check(func, test_container, log_prefix)
        
        # postprocess
        Logger.test(success, prefix)


class RUN:

    @staticmethod
    def run():
        
        Logger.test("running...", log_prefix)

        RUN_JUDGMENT.run()
        
        Logger.test("done", log_prefix)


if __name__ == "__main__":
    RUN.run()
