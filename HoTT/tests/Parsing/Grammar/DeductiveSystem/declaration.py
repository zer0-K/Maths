##############################################
#                                            #
#       Tests on declarations (parsing)      #
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

log_prefix: str = "[Parsing][Grammar][HoTT][declaration]"


class RUN_DECL:

    log_prefix: str = f"{log_prefix}"
    
    @staticmethod
    def var_decl():
        # preprocess
        if True:
            prefix: str = f"{RUN_DECL.log_prefix}[var decl]"

            Logger.test("running...", prefix)
            success: str = "Good"

            test_container = TestContainer()
            test_container.add("var_A oftype Type", 
                               "var_decl\n  var\tvar_A\n  term\n    universe\n")
            
            func: Callable = lambda s: Parser.get_HoTT_tree(s, "var_decl").pretty()
        
        # process
        success = UtilsTest.check(func, test_container, log_prefix)
        
        # postprocess
        Logger.test(success, prefix)

    @staticmethod
    def var_decl_list():
        # preprocess
        if True:
            prefix: str = f"{RUN_DECL.log_prefix}[var decl list]"

            Logger.test("running...", prefix)
            success: str = "Good"

            test_container = TestContainer()
            test_container.add("var_A oftype Type", 
                               "var_decl_list\n  var_decl\n    var\tvar_A\n    term\n      universe\n")
            test_container.add("var_A oftype Type, var_B oftype Type", 
                               "var_decl_list\n  var_decl_list\n    " + \
                               "var_decl\n      var\tvar_A\n      term\n        universe\n  " + \
                               "var_decl\n    var\tvar_B\n    term\n      universe\n")
            
            func: Callable = lambda s: Parser.get_HoTT_tree(s, "var_decl_list").pretty()
        
        # process
        success = UtilsTest.check(func, test_container, log_prefix)
        
        # postprocess
        Logger.test(success, prefix)


class RUN_DEF:

    log_prefix: str = f"{log_prefix}"
    
    @staticmethod
    def var_def():
        # preprocess
        if True:
            prefix: str = f"{RUN_DECL.log_prefix}[var def]"

            Logger.test("running...", prefix)
            success: str = "Good"

            test_container = TestContainer()
            test_container.add("var_A vdef Type oftype Type_1", 
                               "var_def\n  var\tvar_A\n  term\n    universe\n  term\n    universe\t1\n")
            
            func: Callable = lambda s: Parser.get_HoTT_tree(s, "var_def").pretty()
        
        # process
        success = UtilsTest.check(func, test_container, log_prefix)
        
        # postprocess
        Logger.test(success, prefix)


class RUN:

    @staticmethod
    def run():
        
        Logger.test("running...", log_prefix)

        RUN_DECL.var_decl()
        RUN_DECL.var_decl_list()
        
        RUN_DEF.var_def()

        Logger.test("done", log_prefix)


if __name__ == "__main__":
    RUN.run()

