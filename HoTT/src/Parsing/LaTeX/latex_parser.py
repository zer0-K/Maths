###########################################
#                                         #
#       This class parses latex files     #
#                                         #
###########################################


import sys
from lark import Transformer, Tree

proj_dir = "Maths/HoTT".lower()
hott_dir = __file__[:__file__.lower().rfind(proj_dir) + len(proj_dir)]
if hott_dir not in sys.path:
    sys.path = [hott_dir] + sys.path

from src.Parsing.general_parser import Parser


class LatexTransformer(Transformer):

    @staticmethod
    def filter(items, tree_name):
        filtered_items = [item for item in items if item is not None]
        if filtered_items is None or len(filtered_items) == 0:
            return None
        return Tree(tree_name, filtered_items)
 
    def other_content(self, *items):
        return None

    def start(self, items):
        return LatexTransformer.filter(items, "start")
 
    def content(self, items):
        return LatexTransformer.filter(items, "content")

    # ----- definition
    
    def definition(self, items):
        return LatexTransformer.filter(items, "definition") 


class LatexParser:

    parser: Parser = Parser("/home/adrien/Programmation/Projets/Maths/HoTT/src/Parsing/LaTeX/latex.bnf")
    transformer: Transformer = LatexTransformer()
     
    @staticmethod
    def get_latex_grammar_tree():
        parsed_tree = LatexParser.parser.parse_meta()
        return parsed_tree

    @staticmethod
    def get_latex_tree(latex_expr_str: str, start_point_in_grammar: str = "start"):
        parsed = LatexParser.parser.parse(latex_expr_str, start_point_in_grammar, LatexParser.transformer)
        return parsed


if __name__ == "__main__":
    # latex grammar parsed into an AST
    parsed_tree = LatexParser.get_latex_grammar_tree()
    print("Parse Tree (JSON-like):")
    print(parsed_tree)

