#############################################
#                                           #
#      Container for math stuff for UI      #
#                                           #
#############################################

import sys
import traceback
from lark import Tree
from typing import Dict
from collections.abc import Callable

proj_dir = "Maths/HoTT".lower()
hott_dir = __file__[:__file__.lower().rfind(proj_dir) + len(proj_dir)]
if hott_dir not in sys.path:
    sys.path = [hott_dir] + sys.path

from src.Utils.logging import Logger
from src.Parsing.LaTeX.latex_parser import LatexParser

log_prefix: str = "[UI][Math container]"


class MathContainer:
    
    def __init__(self, name: str = "empty container", tree: Tree = None):

        self.name = name
        self.definitions: Dict[str, str] = {}
        self.axioms: Dict[str, str] = {}
        self.theorems: Dict[str, str] = {}
        
        if tree is not None:
            self.transform_ast(tree)
    
    def transform_ast(self, tree: Tree):
        prefix = f"{log_prefix}[transform_ast]({self.name})"

        # check basic integrity
        if True:
            if tree.data != "start" or len(tree.children) == 0:
                Logger.error(f"Cannot transform tree into container, missing node : 'start'", prefix)
                return

            contents = tree.children
            # check content
            if len([False for c in contents if c.data != "content"]) != 0:
                Logger.error(f"Cannot transform tree into container, missing node : 'content'", prefix)
                return
            if len([False for c in contents if len(c.children) != 1]) != 0:
                Logger.error(f"Cannot transform tree into container, a content should have 1 rule", prefix)
                return
            
            # check rules
            rules = [content.children[0] for content in contents]
            if len([False for r in rules if len(r.children) != 1]) != 0:
                Logger.error(f"Cannot transform tree into container, a rule should have 1 child", prefix)
                return
            # 'unwrapping' the rule node
            rules = [r.children[0] for r in rules]
        
        # process : flatten tree
        if True:
            for rule in rules:
                rule_name = rule.data

                if rule_name == "definition":
                    self.add_definition(rule)
        
        # postprocess
        if True:
            Logger.info(f"Latex ast parsed into container", prefix, 6)
    
    def add_definition(self, definition: Tree):
        prefix = f"{log_prefix}[add_definition]({self.name})"
 
        # check integrity
        if True:
            # check if definition contains an id, a notation and the actual definition
            children_names = [c.data.value for c in definition.children]
            if len(definition.children) != 3 \
                    or "def_id" not in children_names \
                    or "notation" not in children_names \
                    or "actual_definition" not in children_names:
                err_msg = f"Cannot retrieve definition from tree: a definitions should have " + \
                    f"a def_id, a notation and an actual_definition. Got : {children_names}"
                Logger.error(err_msg, prefix)
                return                

        # preprocess
        if True:
            def_id = [c.children[0] for c in definition.children if c.data.value == "def_id"][0]
            notation = [c.children[0] for c in definition.children if c.data.value == "notation"][0]
            actual_def = [c.children[0] for c in definition.children if c.data.value == "actual_definition"][0]

            # 'unwrap'
            def_id = def_id.children[0].value
            notation = notation.children[0].value
            actual_def = actual_def.children[0].value
   
         # process
        if True:
            self.definitions[f"{def_id} ::: {notation}"] = actual_def
    
         # postprocess
        if True:
            Logger.info(f"Definition of '{notation}' ({def_id}) added", prefix, 10)
