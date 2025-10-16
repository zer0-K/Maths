#################################################
#                                               #
#       This class parses the HoTT.bnf file     #
#                                               #
#################################################

import sys

grammar_dir = __file__[:__file__.lower().rfind("grammar") + len("grammar")]
sys.path.append(grammar_dir)

from hott_parser import Parser

def example_1():
    # HoTT grammar parsed into an AST
    parsed_tree = Parser.get_HoTT_grammar_tree()
    print("Parse Tree (JSON-like):")
    print(parsed_tree)


def example_2():
    # parse a simple HoTT expression
    parsed = Parser.get_HoTT_tree("Type")
    print(parsed.pretty())

def example_3():
    # parse a simple HoTT expression
    parsed = Parser.get_HoTT_tree("lambda var_x : Type . var_y")
    print(parsed.pretty())


if __name__ == "__main__":
    
    example_1()
    example_2()
    example_3()

    print("end")