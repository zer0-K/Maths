###############################################
#                                             #
#      Container for a math construction      #
#                                             #
###############################################

import sys
import traceback
from lark import Tree, Token
from typing import Dict
from collections.abc import Callable

proj_dir = "Maths/HoTT".lower()
hott_dir = __file__[:__file__.lower().rfind(proj_dir) + len(proj_dir)]
if hott_dir not in sys.path:
    sys.path = [hott_dir] + sys.path

from src.Utils.logging import Logger
from src.Parsing.LaTeX.latex_parser import LatexParser

log_prefix: str = "[UI][Math construction]"


class Construction:
    """Contains all info to build objects from inputs"""

    def __init__(self, name: str, constr_id: str, actual_construction: list):

        self.name = name
        self.constr_id = constr_id
        self.mapping_per_input = {}

        self.init_construction(actual_construction)
    
    def init_construction(self, actual_construction: list):
        prefix = f"{log_prefix}[init_construction]({self.name})"

        # check integrity
        if True:
            # check if the actual construction contains an builder, an input (constructed objects) and a
            # mapping to map the given input to the builder input
            children_names = [c.data.value for c in actual_construction]
            if len(children_names) != 3 \
                    or "apply_builder" not in children_names \
                    or "input_objects" not in children_names \
                    or "out_to_in" not in children_names:
                err_msg = f"Cannot retrieve actual construction from tree: a construction should have " + \
                    f"an apply_builder (a structure that builds objects), input_objects (previously built objects) and " + \
                    f"a out_to_in (mapping of those objects to the builder input). Got : {children_names}"
                Logger.error(err_msg, prefix)
                return                

            builder = [c.children for c in actual_construction if c.data.value == "apply_builder"][0]
            input_objects = [c.children[0] for c in actual_construction if c.data.value == "input_objects"][0]
            input_mapping = [c.children for c in actual_construction if c.data.value == "out_to_in"][0]

        # preprocess
        if True:
            builder_children = [c.children[0].value for c in builder]
            input_objects = [c.children[0].value for c in input_objects.children]
            input_mapping = [c.children[0].value for c in input_mapping]

        # process
        if True:
            nb_inputs_mapped = len(input_mapping)//2
            for i in range(nb_inputs_mapped):
                key = input_mapping[nb_inputs_mapped + i]
                value_nb = input_mapping[i]
                self.mapping_per_input[key] = value_nb
        
        # postprocess
        if True:
            Logger.info(f"Math construction initialized", prefix, 8)

    def construct_derivation(self) -> str:
        return ''
