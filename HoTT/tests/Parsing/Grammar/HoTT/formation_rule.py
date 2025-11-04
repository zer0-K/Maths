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
from src.Parsing.Grammar.hott_parser import HottParser

log_prefix: str = "[Parsing][Grammar][HoTT][formation]"


class RUN_FORM:

    log_prefix: str = f"{log_prefix}"
    
    @staticmethod
    def empty():
        # preprocess
        if True:
            prefix: str = f"{RUN_FORM.log_prefix}[empty type]"

            Logger.test("running...", prefix)
            success: str = "Good"

            test_container = TestContainer()
            test_container.add("empty_type", "formation_rule\n  formation_empty\n")
            
            # starting point in the grammar is the node 'universe'
            func: Callable = lambda s: HottParser.get_HoTT_tree(s, "formation_rule").pretty()
        
        # process
        success = UtilsTest.check(func, test_container, log_prefix)
        
        # postprocess
        Logger.test(success, prefix)

    @staticmethod
    def unit():
        # preprocess
        if True:
            prefix: str = f"{RUN_FORM.log_prefix}[unit type]"

            Logger.test("running...", prefix)
            success: str = "Good"

            test_container = TestContainer()
            test_container.add("unit_type", "formation_rule\n  formation_unit\n")
            
            # starting point in the grammar is the node 'universe'
            func: Callable = lambda s: HottParser.get_HoTT_tree(s, "formation_rule").pretty()
        
        # process
        success = UtilsTest.check(func, test_container, log_prefix)
        
        # postprocess
        Logger.test(success, prefix)

    @staticmethod
    def functions():
        # preprocess
        if True:
            prefix: str = f"{RUN_FORM.log_prefix}[function types]"

            Logger.test("running...", prefix)
            success: str = "Good"

            test_container = TestContainer()
            test_container.add(
                "unit_type \\to unit_type", 
                "formation_rule\n" + \
                "  formation_arrow\n" + \
                "    term\n" + \
                "      formation_rule\n" + \
                "        formation_unit\n" + \
                "    term\n" + \
                "      formation_rule\n" + \
                "        formation_unit\n")
            test_container.add(
                "\\Pi_{var_x:unit_type} star", 
                "formation_rule\n" + \
                "  formation_pi\n" + \
                "    var_decl\n" + \
                "      var\tvar_x\n" + \
                "      term\n" + \
                "        formation_rule\n" + \
                "          formation_unit\n" + \
                "    term\tstar\n")
            
            # starting point in the grammar is the node 'universe'
            func: Callable = lambda s: HottParser.get_HoTT_tree(s, "formation_rule").pretty()
        
        # process
        success = UtilsTest.check(func, test_container, log_prefix)
        
        # postprocess
        Logger.test(success, prefix)

    @staticmethod
    def pair():
        # preprocess
        if True:
            prefix: str = f"{RUN_FORM.log_prefix}[sigma type]"

            Logger.test("running...", prefix)
            success: str = "Good"

            test_container = TestContainer()
            test_container.add(
                "sigma var_x : unit_type.unit_type", 
                "formation_rule\n" + \
                "  formation_sigma\n" + \
                "    var_decl\n" + \
                "      var\tvar_x\n" + \
                "      term\n" + \
                "        formation_rule\n" + \
                "          formation_unit\n" + \
                "    term\n" + \
                "      formation_rule\n" + \
                "        formation_unit\n")
            
            # starting point in the grammar is the node 'universe'
            func: Callable = lambda s: HottParser.get_HoTT_tree(s, "formation_rule").pretty()
        
        # process
        success = UtilsTest.check(func, test_container, log_prefix)
        
        # postprocess
        Logger.test(success, prefix)

    @staticmethod
    def coproduct():
        # preprocess
        if True:
            prefix: str = f"{RUN_FORM.log_prefix}[coproduct type]"

            Logger.test("running...", prefix)
            success: str = "Good"

            test_container = TestContainer()
            test_container.add(
                "unit_type+unit_type", 
                "formation_rule\n" + \
                "  formation_coproduct\n" + \
                "    term\n" + \
                "      formation_rule\n" + \
                "        formation_unit\n" + \
                "    term\n" + \
                "      formation_rule\n" + \
                "        formation_unit\n")
            
            # starting point in the grammar is the node 'universe'
            func: Callable = lambda s: HottParser.get_HoTT_tree(s, "formation_rule").pretty()
        
        # process
        success = UtilsTest.check(func, test_container, log_prefix)
        
        # postprocess
        Logger.test(success, prefix)

    @staticmethod
    def identity():
        # preprocess
        if True:
            prefix: str = f"{RUN_FORM.log_prefix}[unit type]"

            Logger.test("running...", prefix)
            success: str = "Good"

            test_container = TestContainer()
            test_container.add(
                "Id(unit_type, star, star)", 
                "formation_rule\n  formation_id\n" + \
                "    term\n" + \
                "      formation_rule\n" + \
                "        formation_unit\n" + \
                "    term\tstar\n" + \
                "    term\tstar\n")
            
            # starting point in the grammar is the node 'universe'
            func: Callable = lambda s: HottParser.get_HoTT_tree(s, "formation_rule").pretty()
        
        # process
        success = UtilsTest.check(func, test_container, log_prefix)
        
        # postprocess
        Logger.test(success, prefix)

    @staticmethod
    def inductive():
        # preprocess
        if True:
            prefix: str = f"{RUN_FORM.log_prefix}[unit type]"

            Logger.test("running...", prefix)
            success: str = "Good"

            test_container = TestContainer()
            test_container.add(
                "Ind name_List(var_A:Type) : Type where " + \
                    "| name_nil:name_List(var_A) " + \
                    "| name_cons(var_x:var_A, var_xs:name_List(var_A)) :name_List(var_A)", 
                "formation_rule\n" + \
                "  formation_induction\n" + \
                "    name_List\n" + \
                "    params\n" + \
                "      var_decl_list\n" + \
                "        var_decl\n" + \
                "          var\tvar_A\n" + \
                "          term\n" + \
                "            universe\n" + \
                "    term\n" + \
                "      universe\n" + \
                "    constructors\n" + \
                "      constructor\n" + \
                "        name_nil\n" + \
                "        term\n" + \
                "          name_List\n" + \
                "          term\n" + \
                "            var\tvar_A\n" + \
                "      constructor\n" + \
                "        name_cons\n" + \
                "        params\n" + \
                "          var_decl_list\n" + \
                "            var_decl\n" + \
                "              var\tvar_x\n" + \
                "              term\n" + \
                "                var\tvar_A\n" + \
                "            var_decl\n" + \
                "              var\tvar_xs\n" + \
                "              term\n" + \
                "                name_List\n" + \
                "                term\n" + \
                "                  var\tvar_A\n" + \
                "        term\n" + \
                "          name_List\n" + \
                "          term\n" + \
                "            var\tvar_A\n")
            
            # starting point in the grammar is the node 'universe'
            func: Callable = lambda s: HottParser.get_HoTT_tree(s, "formation_rule").pretty()
        
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
        RUN_FORM.functions()
        RUN_FORM.pair()
        RUN_FORM.coproduct()
        RUN_FORM.identity()
        RUN_FORM.inductive()
        
        Logger.test("done", log_prefix)


if __name__ == "__main__":
    RUN.run()

