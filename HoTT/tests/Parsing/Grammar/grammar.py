############################################
#                                          #
#       run tests on the HoTT grammar      #
#                                          #
############################################

import sys

proj_dir = "Maths/HoTT".lower()
hott_dir = __file__[:__file__.lower().rfind(proj_dir) + len(proj_dir)]
if hott_dir not in sys.path:
    sys.path = [hott_dir] + sys.path

from src.Utils.logging import Logger
from tests.Parsing.Grammar.Infrastructure.infrastructure import RUN as RUN_INFRA

log_prefix: str = "[Parsing][Grammar]"


class RUN:
    
    @staticmethod
    def run():
        Logger.test("Running HoTT grammar tests", log_prefix)

        RUN_INFRA.run()
        
        Logger.test("Running HoTT grammar tests     - done", log_prefix)

if __name__ == "__main__":
    RUN.run()
