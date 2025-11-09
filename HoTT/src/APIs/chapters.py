########################################
#                                      #
#       Front end of the main app      #
#                                      #
########################################

from typing import Dict

#
# dictionary acting as a façade to get all the theorems, notations,...
#
chapters: Dict = {
    "Foundations": {
        "Type Theory": "Foundations/TypeTheory/type_theory.tex",
        "Basic constructions": "Foundations/TypeTheory/basic_constructions.tex" 
    }
}

#
# Gives the file corresponding to the chapter number
#
chapter_number: Dict[int, str] = {
    0: chapters["Foundations"]["Type Theory"],
    1: chapters["Foundations"]["Type Theory"],
    2: chapters["Foundations"]["Basic constructions"]
}
