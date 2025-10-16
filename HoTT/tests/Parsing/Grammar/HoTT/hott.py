###############################################
#                                             #
#       run tests on 'pure' hott parsing      #
#                                             #
###############################################

import sys

proj_dir = "Maths/HoTT".lower()
hott_dir = __file__[:__file__.lower().rfind(proj_dir) + len(proj_dir)]
if hott_dir not in sys.path:
    sys.path = [hott_dir] + sys.path

from src.Utils.logging import Logger
from tests.Parsing.Grammar.HoTT.terms_simple import RUN as RUN_TERM
from tests.Parsing.Grammar.HoTT.formation_rule import RUN as RUN_FORM
from tests.Parsing.Grammar.HoTT.introduction_rule import RUN as RUN_INTRO
from tests.Parsing.Grammar.HoTT.elimination_rule import RUN as RUN_ELIM
from tests.Parsing.Grammar.HoTT.computation_rule import RUN as RUN_COMPUT
from tests.Parsing.Grammar.HoTT.terms_complex import RUN as RUN_TERM_COMPLEX

log_prefix: str = "[Parsing][Grammar][HoTT]"


class RUN:
    
    @staticmethod
    def run():
        Logger.test("Running 'pure' HoTT tests", log_prefix)

        RUN_TERM.run()
        RUN_FORM.run()
        RUN_INTRO.run()
        RUN_ELIM.run()
        RUN_COMPUT.run()
        RUN_FORM_COMPLEX.run()
        RUN_INTRO_COMPLEX.run()
        RUN_ELIM_COMPLEX.run()
        RUN_TERM_COMPLEX.run()
        
        Logger.test("Running 'pure' HoTT tests     - done", log_prefix)

if __name__ == "__main__":
    RUN.run()
