##################################################
#                                                #
#       run tests on various HoTT languages      #
#                                                #
##################################################

import sys

proj_dir = "Maths/HoTT".lower()
hott_dir = __file__[:__file__.lower().rfind(proj_dir) + len(proj_dir)]
if hott_dir not in sys.path:
    sys.path = [hott_dir] + sys.path

from src.Utils.logging import Logger
from tests.Parsing.Grammar.grammar import RUN as RUN_GRAMMAR

log_prefix: str = "[Parsing]"


class RUN:
    
    @staticmethod
    def run():
        Logger.test("Running HoTT parsings tests", log_prefix)

        RUN_GRAMMAR.run()
        
        Logger.test("Running HoTT parsings tests     - done", log_prefix)

if __name__ == "__main__":
    RUN.run()
