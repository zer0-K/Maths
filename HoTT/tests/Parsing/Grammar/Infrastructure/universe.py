###########################################
#                                         #
#       Tests on universes (parsing)      #
#                                         #
###########################################

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

log_prefix: str = "[Parsing][Grammar][Infra][universe]"


class RUN_UNIVERSE:

    log_prefix: str = f"{log_prefix}[universe]"
    
    @staticmethod
    def allowed():
        # preprocess
        if True:
            prefix: str = f"{RUN_UNIVERSE.log_prefix}[allowed names]"

            Logger.test("running...", prefix)
            success: str = "Good"

            test_container = TestContainer()
            test_container.add("Type", "universe\n")
            test_container.add("Type_0", "universe\t0\n")
            test_container.add("Type_1", "universe\t1\n")
            test_container.add("Type_10", "universe\t10\n")
            test_container.add("Type_109", "universe\t109\n")
            
            # starting point in the grammar is the node 'universe'
            func: Callable = lambda s: Parser.get_HoTT_tree(s, "universe").pretty()
        
        # process
        success = UtilsTest.check(func, test_container, log_prefix)
        
        # postprocess
        Logger.test(success, prefix)
        

    @staticmethod
    def not_allowed():
        # preprocess
        if True:
            prefix: str = f"{RUN_UNIVERSE.log_prefix}[forbidden names]"

            Logger.test("running...", prefix)
            success: str = "Good"

            test_container = TestContainer()
            test_container.add("Type_", "")
            
            # starting point in the grammar is the node 'universe'
            func: Callable = lambda s: Parser.get_HoTT_tree(s, "universe").pretty()
        
        # process
        success = UtilsTest.check(func, test_container, log_prefix, is_expected_to_fail=True)
        
        # postprocess
        Logger.test(success, prefix)
        

class RUN:

    @staticmethod
    def run():
        
        Logger.test("running...", log_prefix)

        RUN_UNIVERSE.allowed()
        RUN_UNIVERSE.not_allowed()
        
        Logger.test("done", log_prefix)

if __name__ == "__main__":
    RUN.run()
