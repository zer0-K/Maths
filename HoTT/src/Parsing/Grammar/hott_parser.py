#################################################
#                                               #
#       This class parses the HoTT.bnf file     #
#                                               #
#################################################


import sys

proj_dir = "Maths/HoTT".lower()
hott_dir = __file__[:__file__.lower().rfind(proj_dir) + len(proj_dir)]
if hott_dir not in sys.path:
    sys.path = [hott_dir] + sys.path

from src.Parsing.general_parser import Parser


class HottParser:

    parser: Parser = Parser("/home/adrien/Programmation/Projets/Maths/HoTT/src/Parsing/Grammar/HoTT.bnf")
     
    @staticmethod
    def get_HoTT_grammar_tree():
        parsed_tree = HottParser.parser.parse_meta()
        return parsed_tree

    @staticmethod
    def get_HoTT_tree(HoTT_expr_str: str, start_point_in_grammar: str = "inference_system"):
        parsed = HottParser.parser.parse(HoTT_expr_str, start_point_in_grammar)
        return parsed


if __name__ == "__main__":
    # HoTT grammar parsed into an AST
    parsed_tree = HottParser.get_HoTT_grammar_tree()
    print("Parse Tree (JSON-like):")
    print(parsed_tree)
