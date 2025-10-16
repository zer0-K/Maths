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


class RUN_ELIM:

    log_prefix: str = f"{log_prefix}"
    
    @staticmethod
    def empty():
        # preprocess
        if True:
            prefix: str = f"{RUN_ELIM.log_prefix}[empty]"

            Logger.test("running...", prefix)
            success: str = "Good"

            test_container = TestContainer()
            test_container.add(
                "absurd unit_type", 
                "elimination_rule\n" + \
                "  elim_empty\n" + \
                "    term\n" + \
                "      formation_rule\n" + \
                "        formation_unit\n")
            
            # starting point in the grammar is the node 'universe'
            func: Callable = lambda s: Parser.get_HoTT_tree(s, "elimination_rule").pretty()
        
        # process
        success = UtilsTest.check(func, test_container, log_prefix)
        
        # postprocess
        Logger.test(success, prefix)

    @staticmethod
    def unit():
        # preprocess
        if True:
            prefix: str = f"{RUN_ELIM.log_prefix}[unit]"

            Logger.test("running...", prefix)
            success: str = "Good"

            test_container = TestContainer()
            test_container.add(
                "elimT(star,name_c)", 
                "elimination_rule\n" + \
                "  elim_unit\n" + \
                "    term\tstar\n" + \
                "    term\tname_c\n")
            
            # starting point in the grammar is the node 'universe'
            func: Callable = lambda s: Parser.get_HoTT_tree(s, "elimination_rule").pretty()
        
        # process
        success = UtilsTest.check(func, test_container, log_prefix)
        
        # postprocess
        Logger.test(success, prefix)

    @staticmethod
    def func_apply():
        # preprocess
        if True:
            prefix: str = f"{RUN_ELIM.log_prefix}[func_apply]"

            Logger.test("running...", prefix)
            success: str = "Good"

            test_container = TestContainer()
            test_container.add(
                "name_f%(star)", 
                "elimination_rule\n" + \
                "  elim_apply\n" + \
                "    term\tname_f\n" + \
                "    term\tstar\n")
            
            # starting point in the grammar is the node 'universe'
            func: Callable = lambda s: Parser.get_HoTT_tree(s, "elimination_rule").pretty()
        
        # process
        success = UtilsTest.check(func, test_container, log_prefix)
        
        # postprocess
        Logger.test(success, prefix)

    @staticmethod
    def coproduct():
        # preprocess
        if True:
            prefix: str = f"{RUN_ELIM.log_prefix}[coproduct]"

            Logger.test("running...", prefix)
            success: str = "Good"

            test_container = TestContainer()
            test_container.add(
                "case var_s of inl var_x to inl(var_x) | inr var_y to inr(var_y)", 
                "elimination_rule\n" + \
                "  elim_coprod\n" + \
                "    term\n" + \
                "      var\tvar_s\n" + \
                "    elim_coprod_left\n" + \
                "      var\tvar_x\n" + \
                "      term\n" + \
                "        introduction_rule\n" + \
                "          intro_coproduct\n" + \
                "            term\n" + \
                "              var\tvar_x\n" + \
                "    elim_coprod_right\n" + \
                "      var\tvar_y\n" + \
                "      term\n" + \
                "        introduction_rule\n" + \
                "          intro_coproduct\n" + \
                "            term\n" + \
                "              var\tvar_y\n")
            
            # starting point in the grammar is the node 'universe'
            func: Callable = lambda s: Parser.get_HoTT_tree(s, "elimination_rule").pretty()
        
        # process
        success = UtilsTest.check(func, test_container, log_prefix)
        
        # postprocess
        Logger.test(success, prefix)

    @staticmethod
    def sigma():
        # preprocess
        if True:
            prefix: str = f"{RUN_ELIM.log_prefix}[sigma]"

            Logger.test("running...", prefix)
            success: str = "Good"

            test_container = TestContainer()
            test_container.add(
                "pr1((star, star))", 
                "elimination_rule\n" + \
                "  elim_sigma\n" + \
                "    elim_sigma1\n" + \
                "      term\n" + \
                "        introduction_rule\n" + \
                "          intro_pair\n" + \
                "            term\tstar\n" + \
                "            term\tstar\n")
            test_container.add(
                "pr2((star, star))", 
                "elimination_rule\n" + \
                "  elim_sigma\n" + \
                "    elim_sigma2\n" + \
                "      term\n" + \
                "        introduction_rule\n" + \
                "          intro_pair\n" + \
                "            term\tstar\n" + \
                "            term\tstar\n")
            
            # starting point in the grammar is the node 'universe'
            func: Callable = lambda s: Parser.get_HoTT_tree(s, "elimination_rule").pretty()
        
        # process
        success = UtilsTest.check(func, test_container, log_prefix)
        
        # postprocess
        Logger.test(success, prefix)

    @staticmethod
    def path_induction():
        # preprocess
        if True:
            prefix: str = f"{RUN_ELIM.log_prefix}[path induction]"

            Logger.test("running...", prefix)
            success: str = "Good"

            test_container = TestContainer()
            test_container.add(
                "J(var_A, name_a, name_C, name_d, name_b, name_p)", 
                "elimination_rule\n" + \
                "  path_induction\n" + \
                "    term\n" + \
                "      var\tvar_A\n" + \
                "    term\tname_a\n" + \
                "    term\tname_C\n" + \
                "    term\tname_d\n" + \
                "    term\tname_b\n" + \
                "    term\tname_p\n")
            
            # starting point in the grammar is the node 'universe'
            func: Callable = lambda s: Parser.get_HoTT_tree(s, "elimination_rule").pretty()
        
        # process
        success = UtilsTest.check(func, test_container, log_prefix)
        
        # postprocess
        Logger.test(success, prefix)

    @staticmethod
    def recursion():
        # preprocess
        if True:
            prefix: str = f"{RUN_ELIM.log_prefix}[recursion]"

            Logger.test("running...", prefix)
            success: str = "Good"

            test_container = TestContainer()
            test_container.add(
                "rec(name_N, name_comp, name_add, star)", 
                "elimination_rule\n" + \
                "  recursion\n" + \
                "    term\tname_N\n" + \
                "    term\tname_comp\n" + \
                "    term\tname_add\n" + \
                "    term\tstar\n")
            
            # starting point in the grammar is the node 'universe'
            func: Callable = lambda s: Parser.get_HoTT_tree(s, "elimination_rule").pretty()
        
        # process
        success = UtilsTest.check(func, test_container, log_prefix)
        
        # postprocess
        Logger.test(success, prefix)

    @staticmethod
    def induction():
        # preprocess
        if True:
            prefix: str = f"{RUN_ELIM.log_prefix}[induction]"

            Logger.test("running...", prefix)
            success: str = "Good"

            test_container = TestContainer()
            test_container.add(
                "ind(name_N, name_comp, name_add, star)", 
                "elimination_rule\n" + \
                "  induction\n" + \
                "    term\tname_N\n" + \
                "    term\tname_comp\n" + \
                "    term\tname_add\n" + \
                "    term\tstar\n")
            
            # starting point in the grammar is the node 'universe'
            func: Callable = lambda s: Parser.get_HoTT_tree(s, "elimination_rule").pretty()
        
        # process
        success = UtilsTest.check(func, test_container, log_prefix)
        
        # postprocess
        Logger.test(success, prefix)


class RUN:

    @staticmethod
    def run():
        
        Logger.test("running...", log_prefix)

        RUN_ELIM.empty()
        RUN_ELIM.unit()
        RUN_ELIM.func_apply()
        RUN_ELIM.coproduct()
        RUN_ELIM.sigma()
        RUN_ELIM.path_induction()
        RUN_ELIM.recursion()
        RUN_ELIM.induction()
        
        Logger.test("done", log_prefix)


if __name__ == "__main__":
    RUN.run()
