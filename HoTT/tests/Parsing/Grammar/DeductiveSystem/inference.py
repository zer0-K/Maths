##########################################
#                                        #
#       Tests on inferences (parsing)      #
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

log_prefix: str = "[Parsing][Grammar][Logic][inference]"


class RUN_INFERENCE:

    log_prefix: str = f"{log_prefix}"
    
    @staticmethod
    def run():
        # preprocess
        if True:
            prefix: str = f"{RUN_INFERENCE.log_prefix}"

            Logger.test("running...", prefix)
            success: str = "Good"

            test_container = TestContainer()
            # simple axiom
            test_container.add(
                "rule_axiom_1 : \\epsilon ————— empty_context ctx",
                "inference_system\n  rule\n" + \
                "    rule_name\taxiom 1\n" + \
                "    inference_rule\n" + \
                "      premises\t\\epsilon\n" + \
                "      conclusion\n" + \
                "        judgment_list\n" + \
                "          judgment\n" + \
                "            context\tempty_context\n")
            # simple inference rule
            test_container.add(
                "rule_inference_1 : context_gamma ⊢ var_A:Type_i  ————— context_gamma, var_x:var_A ctx,\\quad var_x not in dom(context_gamma)",
                "inference_system\n" + \
                "  rule\n" + \
                "    rule_name\tinference 1\n" + \
                "    inference_rule\n" + \
                "      premises\n" + \
                "        judgment_list\n" + \
                "          judgment\n" + \
                "            context\tcontext_gamma\n" + \
                "            term\n" + \
                "              var\tvar_A\n" + \
                "            term\n" + \
                "              universe\n" + \
                "      conclusion\n" + \
                "        judgment_list\n" + \
                "          judgment\n" + \
                "            context\n" + \
                "              context\tcontext_gamma\n" + \
                "              var_decl\n" + \
                "                var\tvar_x\n" + \
                "                term\n" + \
                "                  var\tvar_A\n" + \
                "          judgment\n" + \
                "            side_condition\n" + \
                "              var_x\n" + \
                "              context\tcontext_gamma\n")
            
            func: Callable = lambda s: HottParser.get_HoTT_tree(s, "inference_system").pretty()
        
        # process
        success = UtilsTest.check(func, test_container, log_prefix)
        
        # postprocess
        Logger.test(success, prefix)


class RUN:

    @staticmethod
    def run():
        
        Logger.test("running...", log_prefix)

        RUN_INFERENCE.run()
        
        Logger.test("done", log_prefix)


if __name__ == "__main__":
    RUN.run()
