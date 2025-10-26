#################################
#                               #
#       Parse a latex file      #
#                               #
#################################

import sys
import traceback
from typing import Dict
from collections.abc import Callable

proj_dir = "Maths/HoTT".lower()
hott_dir = __file__[:__file__.lower().rfind(proj_dir) + len(proj_dir)]
if hott_dir not in sys.path:
    sys.path = [hott_dir] + sys.path

from src.Utils.logging import Logger
from src.UI.latex_to_ui import LatexToUI


class RUN:

    @staticmethod
    def parse_file():
        
        file = "/home/adrien/Programmation/Projets/Maths/HoTT/src/latex/Foundations/TypeTheory/type_theory.tex"
        container =LatexToUI.read_latex(file) 

        Logger.info("end")

if __name__ == "__main__":
    RUN.parse_file()
