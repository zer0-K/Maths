##########################################
#                                        #
#       Test a simple latex parsing      #
#                                        #
##########################################

import sys
import traceback
from typing import Dict
from collections.abc import Callable

proj_dir = "Maths/HoTT".lower()
hott_dir = __file__[:__file__.lower().rfind(proj_dir) + len(proj_dir)]
if hott_dir not in sys.path:
    sys.path = [hott_dir] + sys.path

from src.Utils.logging import Logger
from src.Utils.utils_test import TestContainer, UtilsTest
from src.Parsing.LaTeX.latex_parser import LatexParser

log_prefix: str = "[Parsing][LaTeX][simple]"


class RUN_LATEX:

    log_prefix: str = f"{log_prefix}"
    
    @staticmethod
    def run():
        # preprocess
        if True:
            prefix: str = f"{RUN_LATEX.log_prefix}"

            Logger.test("running...", prefix)
            success: str = "Good"

            test_container = TestContainer()
            test_container.add(
                "\\begin{definition}{1} text \\notation{.} \\probe text \\actualDef{empty context} \\probe \\end{definition}\\end{document}", 
                "start\n" + \
                "  content\n" + \
                "    rule\n" + \
                "      definition\n" + \
                "        def_id\n" + \
                "          text\t1\n" + \
                "        notation\n" + \
                "          text\t.\n" + \
                "        actual_definition\n" + \
                "          text\tempty context\n")
            test_container.add(
                """\\documentclass[12pt]{article}
 
                    \\usepackage{subfiles}
                    \\input{../../preamble} 


                    \\begin{document}

                    \\title{Foundations - type theory}
                    
                    \\maketitle
                    \\tableofcontents

                    \\section{Deductive system}

                    \\subsection{Contexts}

                    \\begin{definition}{0.1}
                    We will note \\notation{.} \\probe for the \\actualDef{empty context} \\probe
                    \\end{definition}
                    
                    \\end{document}
                """, 
                "start\n" + \
                "  content\n" + \
                "    rule\n" + \
                "      definition\n" + \
                "        def_id\n" + \
                "          text\t0.1\n" + \
                "        notation\n" + \
                "          text\t.\n" + \
                "        actual_definition\n" + \
                "          text\tempty context\n" + \
                "  \n\n")
                        
            func: Callable = lambda s: LatexParser.get_latex_tree(s, "start").pretty()
        
        # process
        success = UtilsTest.check(func, test_container, log_prefix)
        
        # postprocess
        Logger.test(success, prefix)


class RUN:

    @staticmethod
    def run():
        
        Logger.test("running...", log_prefix)

        RUN_LATEX.run()
        
        Logger.test("done", log_prefix)


if __name__ == "__main__":
    RUN.run()
