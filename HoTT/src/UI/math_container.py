#############################################
#                                           #
#      Container for math stuff for UI      #
#                                           #
#############################################

import sys
import os
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
from src.UI.tex_container import TexContainer
from src.UI.latex_to_ui import LatexToUI
from src.APIs.chapters import chapter_number_mapping

log_prefix: str = "[UI][Math container]"


class MathContainer:
    """Linker for the files of the library"""
    
    def __init__(self, name: str = "empty container"):

        self.name = name
        self.tex_containers: Dict[str, TexContainer] = {}

    def retrieve_derivation(self, text: str) -> (str, str):
        prefix: str = f"{log_prefix}[retrieve_derivation]({self.name})"
        
        # check integrity
        if True:
            splitted_text = text.split(" -> ")
            if len(splitted_text) != 2:
                Logger.error(f"Text does not have format 'inference_type -> inference_number' : {text}", prefix, 3)
                return None, None
        
        # preprocess
        if True:
            inference_type, inference_id = splitted_text[0], splitted_text[1]
                
        # process
        if True:
            retrieved_text = self.get_from_number(inference_type, inference_id)
                                    
        # postprocess
        if True:
            Logger.info(f"Retrieved text : {inference_type} : {retrieved_text}", prefix, 7)
            return inference_type, retrieved_text

    def get_from_number(self, inference_type: str, inference_id: str) -> str:
        prefix = f"{log_prefix}[get_from_number]({self.name})"
 
        # check integrity
        if True:
            chapter_number = int(inference_id.split(".")[0])
                
            if chapter_number not in chapter_number_mapping.keys():
                Logger.error(f"Chapter number {chapter_number} does not exist", prefix, 3)
                return (None, None)

        # preprocess
        if True:
            chapter_file: str = chapter_number_mapping[chapter_number]
            chapter_file_full: str = os.path.join(hott_dir, "src", "latex", chapter_file)
 
        # process
        if True:
            if chapter_file_full in self.tex_containers.keys():
                tex_container = self.tex_containers[chapter_file_full]
            else:
                tex_container = LatexToUI.read_latex(chapter_file_full)
                self.add_tex(tex_container)
            
            retrieved_text = tex_container.get_from_number(inference_type, inference_id)
    
        # postprocess
        if True:
            return retrieved_text

    def get_tex(self, tex_container_name: str) -> TexContainer:
        prefix = f"{log_prefix}[get_from_number]({self.name})"

        # check integrity
        if tex_container_name not in self.tex_containers.keys():
            Logger.error(
                f"Wrong container selected ({tex_container_name}). Available containers : " +\
                f"{self.tex_containers.keys()}", 
                log_prefix, 
                5)
            return None

        return self.tex_containers[tex_container_name]

    def add_tex(self, tex_container: TexContainer):

        self.tex_containers[tex_container.name] = tex_container
