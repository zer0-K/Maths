################################################################
#                                                              #
#       run tests on the system 'infrastructure' elements      #
#                                                              #
################################################################

import sys

proj_dir = "Maths/HoTT".lower()
hott_dir = __file__[:__file__.lower().rfind(proj_dir) + len(proj_dir)]
if hott_dir not in sys.path:
    sys.path = [hott_dir] + sys.path

from src.Utils.logging import Logger
from tests.Parsing.Grammar.Infrastructure.universe import RUN as RUN_UNIVERSE
from tests.Parsing.Grammar.Infrastructure.variable import RUN as RUN_VAR

log_prefix: str = "[Parsing][Grammar][Infra]"


class RUN:
    
    @staticmethod
    def run():
        Logger.test("Running system 'infrastructure' elements tests", log_prefix)

        RUN_UNIVERSE.run()
        RUN_VAR.run()
        
        Logger.test("Running system 'infrastructure' elements tests     - done", log_prefix)

if __name__ == "__main__":
    RUN.run()
