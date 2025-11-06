###########################################
#                                         #
#       This class parses latex files     #
#                                         #
###########################################


import sys
from lark import Transformer, Tree, Token

proj_dir = "Maths/HoTT".lower()
hott_dir = __file__[:__file__.lower().rfind(proj_dir) + len(proj_dir)]
if hott_dir not in sys.path:
    sys.path = [hott_dir] + sys.path

from src.Parsing.general_parser import Parser


class LatexTransformer(Transformer):

    @staticmethod
    def replace_nested(text: str, command: str, corresponding_hott_command: str = None):
        """Replaces all text in a 'command{text}' by 'command_text'"""
        result = []
        i = 0
        n = len(text)

        if corresponding_hott_command is None:
            corresponding_hott_command = command
        cmd_latex = "\\" + command + "{"
        cmd_size = len(cmd_latex)
        
        while i < n:
            # Look for the \command{ pattern
            
            if text[i:i+cmd_size] == cmd_latex:
                # Add "context_" to result
                result.append(corresponding_hott_command + '\\_{')
                i += cmd_size
                
                # Count brackets to find the matching closing brace
                bracket_count = 1
                content_start = i
                
                while i < n and bracket_count > 0:
                    if text[i] == '{':
                        bracket_count += 1
                    elif text[i] == '}':
                        bracket_count -= 1
                    i += 1
                
                # Extract content (excluding the final closing brace)
                content = text[content_start:i-1]
                
                # Add the content with any internal brackets preserved
                result.append(content)
                result.append('}')
                
            else:
                # Add regular character to result
                result.append(text[i])
                i += 1
        
        return ''.join(result)

    @staticmethod
    def replace_all_commands(text: str):

        text = text.replace("\\ctx", "\\context{\\Gamma}")
        text = text.replace("\\zero", "empty_type")
        text = text.replace("\\unit", "unit_type")
        text = LatexTransformer.replace_nested(text, "context")
        text = LatexTransformer.replace_nested(text, "var")
        text = LatexTransformer.replace_nested(text, "name")
        text = LatexTransformer.replace_nested(text, "U", "Type")
        
        return text

    @staticmethod
    def filter(items, tree_name):
        filtered_items = [item for item in items if item is not None]
        if filtered_items is None or len(filtered_items) == 0:
            return None
        return Tree(tree_name, filtered_items)

    def any_text(self, items):
        token_type = items[0].type
        val = items[0].value.replace("\\text{——}", "—————").replace("\\\\_", "\\_")

        val = LatexTransformer.replace_all_commands(val)
        
        return Tree("any_text", [Token(token_type, val)])

    def other_content(self, *items):
        return None

    def start(self, items):
        return LatexTransformer.filter(items, "start")
 
    def content(self, items):
        return LatexTransformer.filter(items, "content")

    # ----- main nodes
    
    def definition(self, items):
        return LatexTransformer.filter(items, "definition") 

    def axiom(self, items):
        return LatexTransformer.filter(items, "axiom") 


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

