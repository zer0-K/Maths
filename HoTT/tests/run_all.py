#################################
#                               #
#       run all HoTT tests      #
#                               #
#################################

import sys

proj_dir = "Maths/HoTT".lower()
hott_dir = __file__[:__file__.lower().rfind(proj_dir) + len(proj_dir)]
if hott_dir not in sys.path:
    sys.path = [hott_dir] + sys.path

from src.Utils.logging import Logger
from tests.Parsing.parsing import RUN as RUN_PARSING
from tests.UI.ui import RUN as RUN_UI


class RUN:
    
    @staticmethod
    def run():
        Logger.test("Running all tests")

        RUN_PARSING.run()
        RUN_UI.run()
        
        Logger.test("Running all tests     - done")

if __name__ == "__main__":
    RUN.run()
