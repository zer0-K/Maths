############################################
#                                          #
#       Tests on formations (parsing)      #
#                                          #
############################################

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

log_prefix: str = "[Parsing][Grammar][HoTT][formation]"


class RUN_FORM:

    log_prefix: str = f"{log_prefix}[simple]"
    
    @staticmethod
    def empty():
        # preprocess
        if True:
            prefix: str = f"{RUN_FORM.log_prefix}"

            Logger.test("running...", prefix)
            success: str = "Good"

            test_container = TestContainer()
            test_container.add("empty_type", "formation_empty\n")
            
            # starting point in the grammar is the node 'universe'
            func: Callable = lambda s: Parser.get_HoTT_tree(s, "formation_empty").pretty()
        
        # process
        success = UtilsTest.check(func, test_container, log_prefix)
        
        # postprocess
        Logger.test(success, prefix)

    @staticmethod
    def unit():
        # preprocess
        if True:
            prefix: str = f"{RUN_FORM.log_prefix}"

            Logger.test("running...", prefix)
            success: str = "Good"

            test_container = TestContainer()
            test_container.add("unit_type", "formation_unit\n")
            
            # starting point in the grammar is the node 'universe'
            func: Callable = lambda s: Parser.get_HoTT_tree(s, "formation_unit").pretty()
        
        # process
        success = UtilsTest.check(func, test_container, log_prefix)
        
        # postprocess
        Logger.test(success, prefix)


class RUN:

    @staticmethod
    def run():
        
        Logger.test("running...", log_prefix)

        RUN_FORM.empty()
        RUN_FORM.unit()
        
        Logger.test("done", log_prefix)


if __name__ == "__main__":
    RUN.run()

