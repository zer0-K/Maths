######################################
#                                    #
#       Meta grammar definitions     #
#                                    #
######################################

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
    %ignore /--[^\n]*\n/
    %ignore /\/\/[^\n]*\n/
"""

# to get the lark tree in a convenient format
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


class Parser:
    """
    This class has two purposes :
    - parsing a grammar into an AST using the meta-grammar 'BNF_GRAMMAR'
    - parsing the resulting expression into an AST using the underlying grammar
    """
    
    def __init__(self, file_path: str):
        """Retrieve the grammar in BNF format into a string"""
        self.file_path = file_path
        self.bnf_str_meta = ""
        self.bnf_str = ""
        with open(file_path, 'r') as file:
            grammar_str = file.read()
            if grammar_str == "":
                raise Exception(f"BNF at {self.file_path} was not retrieved...")

            self.clean_grammar_str(grammar_str)

    def clean_grammar_str(self, grammar_str):
        self.bnf_str_meta = grammar_str

        # clean the string to have the non-meta bnf
        self.bnf_str = self.bnf_str_meta \
            .replace(r"@ ", "") \
            .replace(r"<", "") \
            .replace(r">", "") \
            .replace("::=", ":")

        self.bnf_str = re.sub("--[^\n]*\n", "\n", self.bnf_str)
        self.bnf_str = re.sub("\/\/[^\n]*\n", "\n", self.bnf_str)
        self.bnf_str = re.sub("[ \t]+", " ", self.bnf_str)
        self.bnf_str = re.sub("\n+", "\n", self.bnf_str)
        self.bnf_str += r"%ignore /[ \t]+/"
        if self.bnf_str[0] == "\n":
            self.bnf_str = self.bnf_str[1:]

        # clean whitespaces for the meta bnf
        self.bnf_str_meta = re.sub(r'[ ]+', r' ', self.bnf_str_meta)
        self.bnf_str_meta = self.bnf_str_meta.replace(r"\n\n", r"\n")

    def parse_meta(self):
        """Get the grammar AST using the meta-grammar 'BNF_GRAMMAR'"""
        if self.bnf_str_meta == "":
            raise Exception(f"BNF at {self.file_path} was not retrieved...")

        parser = lark.Lark(BNF_GRAMMAR, parser="lalr", transformer=BNFTransformer())
        return parser.parse(self.bnf_str_meta)


    def parse(self, expr_str: str, start_point_in_grammar: str = "term"):
        """Get the derivation tree of the given expression"""
        if self.bnf_str == "":
            raise Exception(f"BNF at {self.file_path} was not retrieved...")

        # to parse an actual expression like "lambda x.y"
        parser = lark.Lark(
            self.bnf_str,
            start=start_point_in_grammar,
            parser="lalr",
            transformer=None,  # We'll add a transformer later
        )
        parsed = parser.parse(expr_str)
        return parsed
       
 