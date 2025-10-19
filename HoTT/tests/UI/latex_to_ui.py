###########################################################
#                                                         #
#       Test a simple latex parsing into a container      #
#                                                         #
###########################################################

import sys
import traceback
from typing import Dict
from collections.abc import Callable

proj_dir = "Maths/HoTT".lower()
hott_dir = __file__[:__file__.lower().rfind(proj_dir) + len(proj_dir)]
if hott_dir not in sys.path:
    sys.path = [hott_dir] + sys.path

from src.Utils.logging import Logger
from src.Utils.utils_test import TestContainer, UtilsTest, CST
from src.UI.latex_to_ui import LatexToUI

log_prefix: str = "[UI][Latex to UI container]"


class RUN_LATEX:

    log_prefix: str = f"{log_prefix}"
    
    @staticmethod
    def run():
        # preprocess
        if True:
            prefix: str = f"{RUN_LATEX.log_prefix}"

            Logger.test("running...", prefix)
            success: str = "Good"

            text = "\\begin{definition}{0.1} text \\notation{.} \\probe text \\actualDef{empty context} \\probe \\end{definition}\\end{document}"
        
        # process
        try:
            container = LatexToUI.get_container_from_str(text, "test container")
        except Exception as e:
            err_msg: str = f"{traceback.format_exc()}"
            Logger.error(err_msg, log_prefix, 1)
            success = CST.fail
        
        # postprocess
        if True:

            if container.definitions != {"0.1 ::: .": "empty context"}:
                Logger.error(f"Wrong definition", log_prefix, 3)
                success = CST.fail

            Logger.test(success, prefix)


class RUN:

    @staticmethod
    def run():
        
        Logger.test("running...", log_prefix)

        RUN_LATEX.run()
        
        Logger.test("done", log_prefix)


if __name__ == "__main__":
    RUN.run()
