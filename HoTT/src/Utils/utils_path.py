#############################
#                           #
#       path utilities      #
#                           #
#############################

import sys
import os

proj_dir = "Maths/HoTT".lower()
hott_dir = __file__[:__file__.lower().rfind(proj_dir) + len(proj_dir)]
if hott_dir not in sys.path:
    sys.path = [hott_dir] + sys.path

from src.Utils.logging import Logger


class UtilsPath:
    """Path utilities
    """
    
    @staticmethod
    def get_latex_folder_path() -> str:
        
        return os.path.join(hott_dir, "src", "latex")
