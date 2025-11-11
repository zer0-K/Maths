######################################
#                                    #
#      Transform a latex for UI      #
#                                    #
######################################

import sys
import os
import traceback
from typing import Dict

proj_dir = "Maths/HoTT".lower()
hott_dir = __file__[:__file__.lower().rfind(proj_dir) + len(proj_dir)]
if hott_dir not in sys.path:
    sys.path = [hott_dir] + sys.path

from src.Utils.logging import Logger
from src.Parsing.LaTeX.latex_parser import LatexParser
from src.UI.math_container import MathContainer
from src.APIs.chapters import chapter_number_mapping, chapters

prefix: str = "[UI][Latex to UI]"


class LatexToUI:

    @staticmethod
    def get_container_from_str(text: str, container_name: str) -> MathContainer:
        log_prefix: str = f"{prefix}[get_container_from_str]"

        try:
            tree = LatexParser.get_latex_tree(text)
        except Exception as e:
            err_msg: str = f"Failed to parse lines of {text} as Lark tree for LaTeX.\n{traceback.format_exc()}"
            Logger.error(err_msg, log_prefix, 1)
            return MathContainer()
        
        container = MathContainer(container_name, tree)
        return container
    
    @staticmethod
    def read_latex(file: str) -> MathContainer:
        log_prefix: str = f"{prefix}[read_latex]"
        
        # check integrity
        if True:
            if not os.path.isfile(file):
                Logger.error(f"File {file} does not exist", log_prefix, 3)
                return MathContainer()

            if file[-4:] != ".tex":
                Logger.error(f"File {file} is not a latex file", log_prefix, 3)
                return MathContainer()
        
        # preprocess
        if True:
            # read the latex file
            text = ""
            with open(file, 'r') as f:
                lines = f.readlines()
                Logger.info(f"{len(lines)} lines read from {file}", log_prefix, 10)
                text = ''.join(lines)
            
            i = file[::-1].find("/")
            container_name = file[len(file)-i:-4]
                
        # process
        if True:
            container = LatexToUI.get_container_from_str(text, container_name)
                    
        # postprocess
        if True:
            return container

    @staticmethod
    def retrieve_derivation(text: str, loaded_containers: Dict[str, MathContainer] = None) -> (str, str):
        log_prefix: str = f"{prefix}[retrieve_derivation]"
        
        # check integrity
        if True:
            splitted_text = text.split(" -> ")
            if len(splitted_text) != 2:
                Logger.error(f"Text does not have format 'inference_type -> inference_number' : {text}", log_prefix, 3)
                return (None, None)
            
            inference_type, inference_id = splitted_text[0], splitted_text[1]
            chapter_number = int(inference_id.split(".")[0])
                
            if chapter_number not in chapter_number_mapping.keys():
                Logger.error(f"Chapter number {chapter_number} does not exist", log_prefix, 3)
                return (None, None)
        
        # preprocess
        if True:
            chapter_file = chapter_number_mapping[chapter_number]
            chapter_file_full = os.path.join(hott_dir, "src", "latex", chapter_file)
                
        # process
        if True:
            if loaded_containers is not None and chapter_file_full in loaded_containers.keys():
                container = loaded_containers[chapter_file_full]
            else:
                container = LatexToUI.read_latex(chapter_file_full)

                if loaded_containers is None:
                    loaded_containers = {}
                loaded_containers[container.name] = container
            
            retrieved_text = container.get_from_number(inference_type, inference_id)
                                    
        # postprocess
        if True:
            Logger.info(f"Retrieved text : {inference_type} : {retrieved_text}", log_prefix, 7)
            return inference_type, retrieved_text


if __name__ == "__main__":
    
    text = "\\begin{definition}{0.1} text \\notation{.} \\probe text \\actualDef{empty context} \\probe \\end{definition}\\end{document}"
    container = LatexToUI.get_container_from_str(text, "test container")

    print("end")
