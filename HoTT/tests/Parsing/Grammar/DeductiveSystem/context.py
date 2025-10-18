##########################################
#                                        #
#       Tests on contexts (parsing)      #
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

log_prefix: str = "[Parsing][Grammar][Logic][context]"


class RUN_CTX:

    log_prefix: str = f"{log_prefix}"
    
    @staticmethod
    def run():
        # preprocess
        if True:
            prefix: str = f"{RUN_CTX.log_prefix}"

            Logger.test("running...", prefix)
            success: str = "Good"

            test_container = TestContainer()
            # empty context
            test_container.add("empty_context", "context\tempty_context\n")
            # custom context
            test_container.add("context_gamma", "context\tcontext_gamma\n")
            # extended context
            test_container.add("empty_context, var_A : Type", 
                               "context\n" + \
                               "  context\tempty_context\n" + \
                               "  var_decl\n" + \
                               "    var\tvar_A\n" + \
                               "    term\n" + \
                               "      universe\n")
            # definition context
            test_container.add("empty_context, var_A vdef Type : Type_1", 
                               "context\n" + \
                               "  context\tempty_context\n" + \
                               "  var_def\n" + \
                               "    var\tvar_A\n" + \
                               "    term\n" + \
                               "      universe\n" + \
                               "    term\n" + \
                               "      universe\t1\n")
            
            func: Callable = lambda s: HottParser.get_HoTT_tree(s, "context").pretty()
        
        # process
        success = UtilsTest.check(func, test_container, log_prefix)
        
        # postprocess
        Logger.test(success, prefix)


class RUN:

    @staticmethod
    def run():
        
        Logger.test("running...", log_prefix)

        RUN_CTX.run()
        
        Logger.test("done", log_prefix)


if __name__ == "__main__":
    RUN.run()
