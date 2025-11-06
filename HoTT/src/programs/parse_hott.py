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
    txt = "rule_N-intro-0 : context_{\\Gamma} ctx ————— context_{\\Gamma} ⊢ name_{0}:\\N"
    parsed = HottParser.get_HoTT_tree(txt, "inference_system")

    res_str = parsed.pretty()

    print("end")


if __name__ == "__main__":
    
    run()

    print("end")
