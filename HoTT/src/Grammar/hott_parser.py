#################################################
#                                               #
#       This class parses the HoTT.bnf file     #
#                                               #
#################################################

import os
import lark
import re

# Meta-grammar to parse BNF grammars
BNF_GRAMMAR = r"""
    start: (rule)+
    rule: "@" NAME "::=" alternatives ("|" alternatives)*
    alternatives: term*
    term: STRING | NAME | REGEX | "(" rule ")" 
    NAME: "<" /[a-zA-Z_][a-zA-Z0-9_']*/ ">"
    STRING: /"[^"]*"/ | /'[^']*'/
    REGEX: "/" /[^\/]+/ "/"
    %ignore /\s+/
"""

class BNFTransformer(lark.Transformer):
    def start(self, rules):
        return {"grammar": rules}
    
    def rule(self, items):
        rule_name, *alts = items
        return {"rule": str(rule_name), "productions": alts}
    
    def alternatives(self, terms):
        return {"production": terms}
    
    def term(self, items):
        return {"term": items[0]}

class HottParser:
    
    def __init__(self, file_path: str = "/home/adrien/Programmation/Projets/Maths/HoTT/src/Grammar/HoTT.bnf"):
        """Retrieve the grammar in BNF format into a string"""
        self.file_path = file_path
        self.bnf_str = ""
        with open(file_path, 'r') as file:
            self.bnf_str = file.read()
            if self.bnf_str == "":
                raise Exception(f"BNF at {self.file_path} was not retrieved...")
            self.bnf_str = re.sub("--[^\n]*\n", "", self.bnf_str)
            self.bnf_str = re.sub(r'[ ]+', r' ', self.bnf_str)
            self.bnf_str = self.bnf_str.replace(r"\n\n", r"\n")


    def parse(self):
        if self.bnf_str == "":
            raise Exception(f"BNF at {self.file_path} was not retrieved...")

        parser = lark.Lark(BNF_GRAMMAR, parser="lalr", transformer=BNFTransformer())
        return parser.parse(self.bnf_str)


if __name__ == "__main__":
    parser = HottParser()
    parsed_tree = parser.parse()
    print("Parse Tree (JSON-like):")
    print(parsed_tree)