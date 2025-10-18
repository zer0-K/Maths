#########################################
#                                       #
#       Tests on motives (parsing)      #
#                                       #
#########################################

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

log_prefix: str = "[Parsing][Grammar][Logic][motives]"


class RUN_MOTIVES:

    log_prefix: str = f"{log_prefix}"
    
    @staticmethod
    def pattern():
        # preprocess
        if True:
            prefix: str = f"{RUN_MOTIVES.log_prefix}[pattern]"

            Logger.test("running...", prefix)
            success: str = "Good"

            test_container = TestContainer()
            test_container.add("name_pattern_test", "pattern\tname_pattern_test\n")
            test_container.add("name_pattern_test var_0", 
                               "pattern\n  name_pattern_test\n  varlist\n    var\tvar_0\n")
            
            func: Callable = lambda s: HottParser.get_HoTT_tree(s, "pattern").pretty()
        
        # process
        success = UtilsTest.check(func, test_container, log_prefix)
        
        # postprocess
        Logger.test(success, prefix)

    @staticmethod
    def clause():
        # preprocess
        if True:
            prefix: str = f"{RUN_MOTIVES.log_prefix}[clause]"

            Logger.test("running...", prefix)
            success: str = "Good"

            test_container = TestContainer()
            test_container.add("begclause name_pattern_test to Type", 
                               "clause\n  pattern\tname_pattern_test\n  term\n    universe\n")
            test_container.add("begclause name_pattern_test var_0 to var_1", 
                               "clause\n" + \
                               "  pattern\n" + \
                               "    name_pattern_test\n" + \
                               "    varlist\n" + \
                               "      var\tvar_0\n" + \
                               "  term\n" + \
                               "    var\tvar_1\n")
            
            func: Callable = lambda s: HottParser.get_HoTT_tree(s, "clause").pretty()
        
        # process
        success = UtilsTest.check(func, test_container, log_prefix)
        
        # postprocess
        Logger.test(success, prefix)

    @staticmethod
    def clauses():
        # preprocess
        if True:
            prefix: str = f"{RUN_MOTIVES.log_prefix}[clause list]"

            Logger.test("running...", prefix)
            success: str = "Good"

            test_container = TestContainer()
            test_container.add(
                "[[ begclause name_pattern_test var_0 to var_1 ]]", 
                "clauses\n" + \
                "  clause\n" + \
                "    pattern\n" + \
                "      name_pattern_test\n" + \
                "      varlist\n" + \
                "        var\tvar_0\n" + \
                "    term\n" + \
                "      var\tvar_1\n")
            test_container.add(
                "[[ begclause name_pattern_test var_0 to var_1 begclause name_pattern_test var_0 to var_1 ]]", 
                "clauses\n" + \
                "  clause\n" + \
                "    pattern\n" + \
                "      name_pattern_test\n" + \
                "      varlist\n" + \
                "        var\tvar_0\n" + \
                "    term\n" + \
                "      var\tvar_1\n" + \
                "  clause\n" + \
                "    pattern\n" + \
                "      name_pattern_test\n" + \
                "      varlist\n" + \
                "        var\tvar_0\n" + \
                "    term\n" + \
                "      var\tvar_1\n")
            
            func: Callable = lambda s: HottParser.get_HoTT_tree(s, "clauses").pretty()
        
        # process
        success = UtilsTest.check(func, test_container, log_prefix)
        
        # postprocess
        Logger.test(success, prefix)

    @staticmethod
    def motive():
        # preprocess
        if True:
            prefix: str = f"{RUN_MOTIVES.log_prefix}[motive]"

            Logger.test("running...", prefix)
            success: str = "Good"

            test_container = TestContainer()
            test_container.add("var_0 : Type to Type", 
                               "motive\n  var\tvar_0\n  term\n    universe\n  term\n    universe\n")
            test_container.add("var_0 : var_1 to Type", 
                               "motive\n  var\tvar_0\n  term\n    var\tvar_1\n  term\n    universe\n")
            
            func: Callable = lambda s: HottParser.get_HoTT_tree(s, "motive").pretty()
        
        # process
        success = UtilsTest.check(func, test_container, log_prefix)
        
        # postprocess
        Logger.test(success, prefix)

    @staticmethod
    def motives():
        # preprocess
        if True:
            prefix: str = f"{RUN_MOTIVES.log_prefix}[motives]"

            Logger.test("running...", prefix)
            success: str = "Good"

            test_container = TestContainer()
            test_container.add(
                "{ var_0 : Type to Type }", 
                "motives\n" + \
                "  motive\n" + \
                "    var\tvar_0\n" + \
                "    term\n" + \
                "      universe\n" + \
                "    term\n" + \
                "      universe\n")
            test_container.add(
                "{ var_0 : Type to Type ; var_0 : var_1 to Type }", 
                "motives\n" + \
                "  motive\n" + \
                "    var\tvar_0\n" + \
                "    term\n" + \
                "      universe\n" + \
                "    term\n" + \
                "      universe\n" + \
                "  motive\n" + \
                "    var\tvar_0\n" + \
                "    term\n" + \
                "      var\tvar_1\n" + \
                "    term\n" + \
                "      universe\n")
            
            func: Callable = lambda s: HottParser.get_HoTT_tree(s, "motives").pretty()
        
        # process
        success = UtilsTest.check(func, test_container, log_prefix)
        
        # postprocess
        Logger.test(success, prefix)


class RUN:

    @staticmethod
    def run():
        
        Logger.test("running...", log_prefix)

        RUN_MOTIVES.pattern()
        RUN_MOTIVES.clause()
        RUN_MOTIVES.clauses()
        RUN_MOTIVES.motive()
        RUN_MOTIVES.motives()
        
        Logger.test("done", log_prefix)


if __name__ == "__main__":
    RUN.run()

