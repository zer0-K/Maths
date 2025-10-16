###############################################
#                                             #
#       Tests on introductions (parsing)      #
#                                             #
###############################################

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

log_prefix: str = "[Parsing][Grammar][HoTT][introduction]"


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
            test_container.add("star:unit_type", "introduction_rule\n  intro_unit\tstar\n")
            
            func: Callable = lambda s: Parser.get_HoTT_tree(s, "introduction_rule").pretty()
        
        # process
        success = UtilsTest.check(func, test_container, log_prefix)
        
        # postprocess
        Logger.test(success, prefix)

    @staticmethod
    def function():
        # preprocess
        if True:
            prefix: str = f"{RUN_INTRO.log_prefix}"

            Logger.test("running...", prefix)
            success: str = "Good"

            test_container = TestContainer()
            test_container.add(
                "lambda var_x:unit_type.star", 
                "introduction_rule\n" + \
                "  intro_lambda\n" + \
                "    var_decl\n" + \
                "      var\tvar_x\n" + \
                "      term\n" + \
                "        formation_rule\n" + \
                "          formation_unit\n" + \
                "    term\tstar\n")
            
            func: Callable = lambda s: Parser.get_HoTT_tree(s, "introduction_rule").pretty()
        
        # process
        success = UtilsTest.check(func, test_container, log_prefix)
        
        # postprocess
        Logger.test(success, prefix)

    @staticmethod
    def pair():
        # preprocess
        if True:
            prefix: str = f"{RUN_INTRO.log_prefix}"

            Logger.test("running...", prefix)
            success: str = "Good"

            test_container = TestContainer()
            test_container.add(
                "(star,star)", 
                "introduction_rule\n" + \
                "  intro_pair\n" + \
                "    term\tstar\n" + \
                "    term\tstar\n")
            
            func: Callable = lambda s: Parser.get_HoTT_tree(s, "introduction_rule").pretty()
        
        # process
        success = UtilsTest.check(func, test_container, log_prefix)
        
        # postprocess
        Logger.test(success, prefix)

    @staticmethod
    def coproduct():
        # preprocess
        if True:
            prefix: str = f"{RUN_INTRO.log_prefix}"

            Logger.test("running...", prefix)
            success: str = "Good"

            test_container = TestContainer()
            test_container.add("inl star", 
                               "introduction_rule\n  intro_coproduct\n    term\tstar\n")
            test_container.add("inr star", 
                               "introduction_rule\n  intro_coproduct\n    term\tstar\n")
            
            func: Callable = lambda s: Parser.get_HoTT_tree(s, "introduction_rule").pretty()
        
        # process
        success = UtilsTest.check(func, test_container, log_prefix)
        
        # postprocess
        Logger.test(success, prefix)

    @staticmethod
    def reflexion():
        # preprocess
        if True:
            prefix: str = f"{RUN_INTRO.log_prefix}"

            Logger.test("running...", prefix)
            success: str = "Good"

            test_container = TestContainer()
            test_container.add("refl(star)", 
                               "introduction_rule\n  intro_refl\n    term\tstar\n")
            
            func: Callable = lambda s: Parser.get_HoTT_tree(s, "introduction_rule").pretty()
        
        # process
        success = UtilsTest.check(func, test_container, log_prefix)
        
        # postprocess
        Logger.test(success, prefix)

    @staticmethod
    def constructor():
        # preprocess
        if True:
            prefix: str = f"{RUN_INTRO.log_prefix}"

            Logger.test("running...", prefix)
            success: str = "Good"

            test_container = TestContainer()
            test_container.add(
                "name_cons(var_x:var_A, var_xs:name_List(var_A)) :name_List(var_A)", 
                "introduction_rule\n" + \
                "  intro_constr\n" + \
                "    constructor\n" + \
                "      name_cons\n" + \
                "      params\n" + \
                "        var_decl_list\n" + \
                "          var_decl\n" + \
                "            var\tvar_x\n" + \
                "            term\n" + \
                "              var\tvar_A\n" + \
                "          var_decl\n" + \
                "            var\tvar_xs\n" + \
                "            term\n" + \
                "              name_List\n" + \
                "              term\n" + \
                "                var\tvar_A\n" + \
                "      term\n" + \
                "        name_List\n" + \
                "        term\n" + \
                "          var\tvar_A\n")
            
            func: Callable = lambda s: Parser.get_HoTT_tree(s, "introduction_rule").pretty()
        
        # process
        success = UtilsTest.check(func, test_container, log_prefix)
        
        # postprocess
        Logger.test(success, prefix)


class RUN:

    @staticmethod
    def run():
        
        Logger.test("running...", log_prefix)

        RUN_INTRO.unit()
        RUN_INTRO.function()
        RUN_INTRO.pair()
        RUN_INTRO.coproduct()
        RUN_INTRO.reflexion()
        RUN_INTRO.constructor()
        
        Logger.test("done", log_prefix)


if __name__ == "__main__":
    RUN.run()
