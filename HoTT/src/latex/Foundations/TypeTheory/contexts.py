#############################
#                           #
#       Context axioms      #
#                           #
#############################

import sys
import traceback
from typing import Dict
from collections.abc import Callable

proj_dir = "Maths/HoTT".lower()
hott_dir = __file__[:__file__.lower().rfind(proj_dir) + len(proj_dir)]
if hott_dir not in sys.path:
    sys.path = [hott_dir] + sys.path

from src.Utils.logging import Logger
from src.Parsing.Grammar.hott_parser import HottParser

log_prefix: str = "[Foundations][Type Theory][contexts]"

axioms: Dict[str, str] = {
    "empty context": "rule_empty_ctx: epsilon ————— empty_context ctx",
    "context extension": "rule_ext_ctx : context_gamma ⊢ var_A:Type_i  ————— context_gamma, var_x:var_A ctx, var_x not in dom(context_gamma)"
}

class RUN:

    @staticmethod
    def run():
        
        Logger.test("running...", log_prefix)

        parsed = HottParser.get_HoTT_tree(axioms["empty context"], "inference_system")
        parsed = HottParser.get_HoTT_tree(axioms["context extension"], "inference_system")

        Logger.test("done", log_prefix)


if __name__ == "__main__":
    RUN.run()
