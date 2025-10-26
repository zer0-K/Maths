#################################################
#                                               #
#       This class parses the HoTT.bnf file     #
#                                               #
#################################################


import sys
from lark import Transformer, Tree, Token

proj_dir = "Maths/HoTT".lower()
hott_dir = __file__[:__file__.lower().rfind(proj_dir) + len(proj_dir)]
if hott_dir not in sys.path:
    sys.path = [hott_dir] + sys.path

from src.Parsing.general_parser import Parser


class HottTransformer(Transformer):

    @staticmethod
    def filter(items, tree_name):
        filtered_items = [item for item in items if item is not None]
        if filtered_items is None or len(filtered_items) == 0:
            return None
        return Tree(tree_name, filtered_items)
 
    def rule_name(self, items):
        rule_name = items[0].value.replace("rule_", "").replace("_", " ")
        t = Tree("rule_name", [Token("RULE_NAME", rule_name)])
        return t 


class HottParser:

    parser: Parser = Parser("/home/adrien/Programmation/Projets/Maths/HoTT/src/Parsing/Grammar/HoTT.bnf")
    transformer: Transformer = HottTransformer()

    @staticmethod
    def get_HoTT_grammar_tree():
        parsed_tree = HottParser.parser.parse_meta()
        return parsed_tree

    @staticmethod
    def get_HoTT_tree(HoTT_expr_str: str, start_point_in_grammar: str = "inference_system"):
        parsed = HottParser.parser.parse(HoTT_expr_str, start_point_in_grammar, HottParser.transformer)
        return parsed


if __name__ == "__main__":
    # HoTT grammar parsed into an AST
    parsed_tree = HottParser.get_HoTT_grammar_tree()
    print("Parse Tree (JSON-like):")
    print(parsed_tree)
