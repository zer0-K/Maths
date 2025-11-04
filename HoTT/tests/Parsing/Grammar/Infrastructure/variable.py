###########################################
#                                         #
#       Tests on variables (parsing)      #
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
from src.Parsing.Grammar.hott_parser import HottParser

log_prefix: str = "[Parsing][Grammar][Infra][variable]"


class RUN_VAR:

    log_prefix: str = f"{log_prefix}[variable]"
    
    @staticmethod
    def allowed():
        # preprocess
        if True:
            prefix: str = f"{RUN_VAR.log_prefix}[allowed names]"

            Logger.test("running...", prefix)
            success: str = "Good"

            test_container = TestContainer()
            test_container.add("var_0", "var\tvar_0\n")
            test_container.add("var_{\\Gamma}", "var\tvar_{\\Gamma}\n")
            test_container.add("var_test", "var\tvar_test\n")
            test_container.add("var_test_0", "var\tvar_test_0\n")
            test_container.add("var_test1_0", "var\tvar_test1_0\n")

            # starting point in the grammar is the node 'var'
            func: Callable = lambda s: HottParser.get_HoTT_tree(s, "var").pretty()
        
        # process
        success = UtilsTest.check(func, test_container, log_prefix)
        
        # postprocess
        Logger.test(success, prefix)

    @staticmethod
    def not_allowed():
        # preprocess
        if True:
            prefix: str = f"{RUN_VAR.log_prefix}[forbidden names]"

            Logger.test("running...", prefix)
            success: str = "Good"

            test_container = TestContainer()
            test_container.add("var", "")
            test_container.add("var_", "")
            
            # starting point in the grammar is the node 'var'
            func: Callable = lambda s: HottParser.get_HoTT_tree(s, "var").pretty()
        
        # process
        success = UtilsTest.check(func, test_container, log_prefix, is_expected_to_fail=True)
        
        # postprocess
        Logger.test(success, prefix)
        

class RUN_VAR_LIST:

    log_prefix: str = f"{log_prefix}[variable list]"
    
    @staticmethod
    def allowed():
        # preprocess
        if True:
            prefix: str = f"{RUN_VAR.log_prefix}"

            Logger.test("running...", prefix)
            success: str = "Good"

            test_container = TestContainer()
            test_container.add("var_0", "varlist\n  var\tvar_0\n")
            test_container.add("var_0, var_1", "varlist\n  var\tvar_0\n  var\tvar_1\n")
            test_container.add("var_0, var_1, var_2", 
                               "varlist\n  var\tvar_0\n  var\tvar_1\n  var\tvar_2\n")

            func: Callable = lambda s: HottParser.get_HoTT_tree(s, "varlist").pretty()
        
        # process
        success = UtilsTest.check(func, test_container, log_prefix)
        
        # postprocess
        Logger.test(success, prefix)


class RUN:

    @staticmethod
    def run():
        
        Logger.test("running...", log_prefix)

        RUN_VAR.allowed()
        RUN_VAR.not_allowed()
        
        RUN_VAR_LIST.allowed()
        
        Logger.test("done", log_prefix)


if __name__ == "__main__":
    RUN.run()
