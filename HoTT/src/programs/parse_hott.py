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
    # parse an HoTT expression
    txt = "rule_test : context_{\\Gamma} ⊢ var_{a}:var_{A}, context_{\\Gamma} ⊢ var_{A}\\equiv var_{B}:Type_{i} ————— context_{\\Gamma} ⊢ var_{a}:var_{B}"
    parsed = HottParser.get_HoTT_tree(txt, "inference_system")

    res_str = parsed.pretty()

    print("end")


if __name__ == "__main__":
    
    run()

    print("end")
