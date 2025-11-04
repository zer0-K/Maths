######################################
#                                    #
#      Transform a latex for UI      #
#                                    #
######################################

import sys
import os
import traceback

proj_dir = "Maths/HoTT".lower()
hott_dir = __file__[:__file__.lower().rfind(proj_dir) + len(proj_dir)]
if hott_dir not in sys.path:
    sys.path = [hott_dir] + sys.path

from src.Utils.logging import Logger
from src.Parsing.LaTeX.latex_parser import LatexParser
from src.UI.math_container import MathContainer

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


if __name__ == "__main__":
    
    text = "\\begin{definition}{0.1} text \\notation{.} \\probe text \\actualDef{empty context} \\probe \\end{definition}\\end{document}"
    container = LatexToUI.get_container_from_str(text, "test container")

    print("end")
