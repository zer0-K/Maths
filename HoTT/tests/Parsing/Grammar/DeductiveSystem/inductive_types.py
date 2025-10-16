#################################################
#                                               #
#       Tests on inductive types (parsing)      #
#                                               #
#################################################

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

log_prefix: str = "[Parsing][Grammar][Logic][inductive_types]"


class RUN_IND:

    log_prefix: str = f"{log_prefix}"
    
    @staticmethod
    def params():
        # preprocess
        if True:
            prefix: str = f"{RUN_IND.log_prefix}"

            Logger.test("running...", prefix)
            success: str = "Good"

            test_container = TestContainer()
            test_container.add(
                "(var_A : Type)", 
                "params\n" + \
                "  var_decl_list\n" + \
                "    var_decl\n" + \
                "      var\tvar_A\n" + \
                "      term\n" + \
                "        universe\n")
            test_container.add(
                "(var_A : Type, var_B : Type)", 
                "params\n" + \
                "  var_decl_list\n" + \
                "    var_decl\n" + \
                "      var\tvar_A\n" + \
                "      term\n" + \
                "        universe\n" + \
                "    var_decl\n" + \
                "      var\tvar_B\n" + \
                "      term\n" + \
                "        universe\n")
            
            func: Callable = lambda s: Parser.get_HoTT_tree(s, "params").pretty()
        
        # process
        success = UtilsTest.check(func, test_container, log_prefix)
        
        # postprocess
        Logger.test(success, prefix)

    @staticmethod
    def constructor():
        # preprocess
        if True:
            prefix: str = f"{RUN_IND.log_prefix}"

            Logger.test("running...", prefix)
            success: str = "Good"

            test_container = TestContainer()
            test_container.add("name_new_el : var_A", 
                               "constructor\n  name_new_el\n  term\n    var\tvar_A\n")
            test_container.add(
                "name_C(var_A:Type, var_B:Type) : var_A", 
                "constructor\n" + \
                "  name_C\n" + \
                "  params\n" + \
                "    var_decl_list\n" + \
                "      var_decl\n" + \
                "        var\tvar_A\n" + \
                "        term\n" + \
                "          universe\n" + \
                "      var_decl\n" + \
                "        var\tvar_B\n" + \
                "        term\n" + \
                "          universe\n" + \
                "  term\n" + \
                "    var\tvar_A\n")
            
            func: Callable = lambda s: Parser.get_HoTT_tree(s, "constructor").pretty()
        
        # process
        success = UtilsTest.check(func, test_container, log_prefix)
        
        # postprocess
        Logger.test(success, prefix)

    @staticmethod
    def constructors():
        # preprocess
        if True:
            prefix: str = f"{RUN_IND.log_prefix}"

            Logger.test("running...", prefix)
            success: str = "Good"

            test_container = TestContainer()
            test_container.add(
                "| name_C(var_A:Type, var_B:Type) :var_A", 
                "constructors\n" + \
                "  constructor\n" + \
                "    name_C\n" + \
                "    params\n" + \
                "      var_decl_list\n" + \
                "        var_decl\n" + \
                "          var\tvar_A\n" + \
                "          term\n" + \
                "            universe\n" + \
                "        var_decl\n" + \
                "          var\tvar_B\n" + \
                "          term\n" + \
                "            universe\n" + \
                "    term\n" + \
                "      var\tvar_A\n")
            test_container.add(
                "| name_C1(var_A:Type) :var_A " + \
                    "| name_C2(var_A:Type, var_B:Type) :var_A", 
                "constructors\n" + \
                "  constructor\n" + \
                "    name_C1\n" + \
                "    params\n" + \
                "      var_decl_list\n" + \
                "        var_decl\n" + \
                "          var\tvar_A\n" + \
                "          term\n" + \
                "            universe\n" + \
                "    term\n" + \
                "      var\tvar_A\n" + \
                "  constructor\n" + \
                "    name_C2\n" + \
                "    params\n" + \
                "      var_decl_list\n" + \
                "        var_decl\n" + \
                "          var\tvar_A\n" + \
                "          term\n" + \
                "            universe\n" + \
                "        var_decl\n" + \
                "          var\tvar_B\n" + \
                "          term\n" + \
                "            universe\n" + \
                "    term\n" + \
                "      var\tvar_A\n")
            
            func: Callable = lambda s: Parser.get_HoTT_tree(s, "constructors").pretty()
        
        # process
        success = UtilsTest.check(func, test_container, log_prefix)
        
        # postprocess
        Logger.test(success, prefix)


class RUN:

    @staticmethod
    def run():
        
        Logger.test("running...", log_prefix)

        RUN_IND.params()
        RUN_IND.constructor()
        RUN_IND.constructors()
        
        Logger.test("done", log_prefix)


if __name__ == "__main__":
    RUN.run()

