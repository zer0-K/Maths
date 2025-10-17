#####################################################
#                                                   #
#       run tests on hott logic system parsing      #
#                                                   #
#####################################################

import sys

proj_dir = "Maths/HoTT".lower()
hott_dir = __file__[:__file__.lower().rfind(proj_dir) + len(proj_dir)]
if hott_dir not in sys.path:
    sys.path = [hott_dir] + sys.path

from src.Utils.logging import Logger
from tests.Parsing.Grammar.DeductiveSystem.context import RUN as RUN_CONTEXT
from tests.Parsing.Grammar.DeductiveSystem.declaration import RUN as RUN_DECL
from tests.Parsing.Grammar.DeductiveSystem.motives import RUN as RUN_MOTIVES
from tests.Parsing.Grammar.DeductiveSystem.inductive_types import RUN as RUN_IND_TYPES
from tests.Parsing.Grammar.DeductiveSystem.judgment import RUN as RUN_JUDGMENT
from tests.Parsing.Grammar.DeductiveSystem.inference import RUN as RUN_INFERENCE

log_prefix: str = "[Parsing][Grammar][Logic]"


class RUN:
    
    @staticmethod
    def run():
        Logger.test("Running HoTT logic system tests", log_prefix)

        RUN_CONTEXT.run()
        RUN_DECL.run()
        RUN_MOTIVES.run()
        RUN_IND_TYPES.run()
        RUN_JUDGMENT.run()
        RUN_INFERENCE.run()
        
        Logger.test("Running HoTT logic system tests     - done", log_prefix)

if __name__ == "__main__":
    RUN.run()
