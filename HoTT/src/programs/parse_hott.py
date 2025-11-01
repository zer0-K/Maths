################################
#                              #
#       Parses a HoTT text     #
#                              #
################################

import sys

proj_dir = "Maths/HoTT".lower()
hott_dir = __file__[:__file__.lower().rfind(proj_dir) + len(proj_dir)]
if hott_dir not in sys.path:
    sys.path = [hott_dir] + sys.path

from src.Parsing.Grammar.hott_parser import HottParser


def run():
    # parse a simple HoTT expression
    txt = "rule_context_extension : context_\Gamma ⊢ var_A:Type_i ————— context_\Gamma, var_x:var_A ctx, var_x not in dom(context_\Gamma)"
    parsed = HottParser.get_HoTT_tree(txt, "inference_system")

    res_str = parsed.pretty()

    print("end")


if __name__ == "__main__":
    
    run()

    print("end")
