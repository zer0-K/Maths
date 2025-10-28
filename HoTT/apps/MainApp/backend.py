#######################################
#                                     #
#       Back end of the main app      #
#                                     #
#######################################

import sys
import os
import streamlit as st
from typing import Dict

proj_dir = "Maths/HoTT".lower()
hott_dir = __file__[:__file__.lower().rfind(proj_dir) + len(proj_dir)]
if hott_dir not in sys.path:
    sys.path = [hott_dir] + sys.path

from src.Utils.logging import Logger
from src.Utils.utils_path import UtilsPath
from src.APIs.chapters import chapters
from src.UI.latex_to_ui import LatexToUI
from src.UI.math_container import MathContainer


class BackEnd:
    
    log_prefix: str = "[MainApp][BackEnd]"

    @staticmethod
    def init(session):

        # preprocess
        if True:
            log_prefix: str = f"{BackEnd.log_prefix}[init]"

            Logger.log_level = 1000
            Logger.info(f"Initializing environment", log_prefix, 10)
        
        # process
        if True:
            Logger.info(f"Initializing chapters", log_prefix, 10)
            session = BackEnd.Data.update_subchapters(session)
        
        return session
    
    class Data:
           
        @staticmethod
        def load() -> Dict:
            data = {
                "chapters": chapters,
                "selected_chapter_path": [""],
                "subchapters": [],
                "selected_chapter_tex_file": "",
                "math_container": MathContainer(),
                # choices and display
                "definition_choices": {},
                "axiom_choices": {},
                "display_text": ""
            }
            
            return data
        
        @staticmethod
        def update_subchapters(session):

            # preprocess
            if True:
                log_prefix: str = f"{BackEnd.log_prefix}[Data][get_subchapters]"
            
                chapter_path: list[str] = session["data"]["selected_chapter_path"]

                subtree: Dict = chapters 
            
            # process
            if True:
                for chapter in chapter_path[1:]:
                    if chapter not in subtree.keys():
                        Logger.error(f"Chapter {chapter} not found in chapters. " + \
                                        f"Available chapters: {subtree.keys()}", 
                                    log_prefix)
                        return session
                    subtree = subtree[chapter]

            # postprocess
            if True:
                if isinstance(subtree, dict):
                    current_chapters: list[str] = list(subtree.keys())
                else:
                    # leaves of the tree are file paths
                    latex_file_path = subtree
                    if isinstance(latex_file_path, str):
                        full_path = os.path.join(UtilsPath.get_latex_folder_path(), latex_file_path)
                        session["data"]["selected_chapter_tex_file"] = full_path
                    current_chapters = []
                session["data"]["subchapters"] = ["None"] + current_chapters

                Logger.info(f"Retrieved chapters: {current_chapters}", log_prefix, 15)

                return session

    class Get:
        
        class Choices:

            @staticmethod
            def definition_choices(session) -> list[str]:
                # preprocess
                if True:
                    log_prefix: str = f"{BackEnd.log_prefix}[Listener][definition_choices]"
                    container: MathContainer = st.session_state["data"]["math_container"]
                    definitions: Dict[str, str] = container.definitions
                    choices = []
                
                # process
                if len(definitions) > 0:
                    choices = list(definitions.keys())

                # postprocess
                if True:
                    return choices

            @staticmethod
            def axiom_choices(session) -> list[str]:
                # preprocess
                if True:
                    log_prefix: str = f"{BackEnd.log_prefix}[Listener][axiom_choices]"
                    container: MathContainer = st.session_state["data"]["math_container"]
                    axioms: Dict[str, str] = container.axioms
                    choices = []
                
                # process
                if len(axioms) > 0:
                    choices = list(axioms.keys())

                # postprocess
                if True:
                    return choices

    class Listener:
        
        class Chapters:
            
            @staticmethod
            def on_select_subchapter(session):
                
                # preprocess
                if True:
                    
                    log_prefix: str = f"{BackEnd.log_prefix}[Listener][on_selected_subchapter]"

                    subchapter: str = session.selectbox_subchapter
                    if subchapter == "None":
                        return session
                    
                    Logger.info(f"Chapter selected: {subchapter}", log_prefix, 15)

                # process
                if True:
                    session["data"]["selected_chapter_path"].append(subchapter)
                    session = BackEnd.Data.update_subchapters(session) 
                
                # postprocess
                if True:
                    return session
            
            @staticmethod
            def on_previous_chapter(session):
                
                # preprocess
                if True:
                    
                    log_prefix: str = f"{BackEnd.log_prefix}[Listener][on_previous_chapter]"

                    Logger.info(f"Going to previous chapter", log_prefix, 15)
                    subchapters = session["data"]["selected_chapter_path"]

                # process
                if True:
                    if len(subchapters) > 1:
                        session["data"]["selected_chapter_path"] = subchapters[:-1]
                        session = BackEnd.Data.update_subchapters(session)
                    else:
                        Logger.warn("There is no subchapter", log_prefix, 10)
                
                # postprocess
                if True:
                    return session
            
            @staticmethod
            def on_parse_latex(session):
                
                # preprocess
                if True:
                    log_prefix: str = f"{BackEnd.log_prefix}[Listener][on_parse_latex]"
                    file: str = st.session_state["data"]["selected_chapter_tex_file"]
                
                # process
                if True:
                    container = LatexToUI.read_latex(file)
                    session["data"]["math_container"] = container
                    
                    # updates choices after latex file was parsed
                    # definitions
                    if True:
                        def_choices_raw = BackEnd.Get.Choices.definition_choices(st.session_state)
                        def_choices_clean = [d.replace(":::", ":").replace("$", "") for d in def_choices_raw]
                        def_choices_display = {d1: d2 for d1, d2 in zip(def_choices_clean, def_choices_raw)}
                        session["data"]["definition_choices"] = def_choices_display
                    # axioms
                    if True:
                        axiom_choices_raw = BackEnd.Get.Choices.axiom_choices(st.session_state)
                        axiom_choices_clean = [a.replace(":::", ":").replace("$", "") for a in axiom_choices_raw]
                        axiom_choices_display = {a1: a2 for a1, a2 in zip(axiom_choices_clean, axiom_choices_raw)}
                        session["data"]["axiom_choices"] = axiom_choices_display

                # postprocess
                if True:
                    Logger.debug(f"Definition choices: {def_choices_clean}", log_prefix, 5)
                    Logger.debug(f"Axiom choices: {axiom_choices_clean}", log_prefix, 5)
                    return session
        
        class Choices:

            @staticmethod
            def on_select_definition(session):

                # preprocess
                if True:
                    log_prefix: str = f"{BackEnd.log_prefix}[Listener][on_select_definition]"

                    container = session["data"]["math_container"]
                    choice_displayed = session["selectbox_definition"]
                    choice = session["data"]["definition_choices"][choice_displayed]

                # process
                if True:
                    def_id, notation = choice.split(":::")
                    def_id = def_id.replace(" ", "")
                    Logger.debug(f"Chosen definition: id={def_id}, notation={notation}", log_prefix, 5)
                    actual_def = container.definitions[choice]

                    display_text = BackEnd.Display.clean_definition(def_id, notation, actual_def)
                    session["data"]["display_text"] = display_text
                
                # postprocess
                if True:
                    return session

            @staticmethod
            def on_select_axiom(session):

                # preprocess
                if True:
                    log_prefix: str = f"{BackEnd.log_prefix}[Listener][on_select_axiom]"

                    container = session["data"]["math_container"]
                    choice_displayed = session["selectbox_axioms"]
                    choice = session["data"]["axiom_choices"][choice_displayed]

                # process
                if True:
                    axiom_id, axiom_name = choice.split(":::")
                    axiom_id = axiom_id.replace(" ", "")
                    Logger.debug(f"Chosen axiom: id={axiom_id}, axiom name={axiom_name}", log_prefix, 5)
                    actual_axiom = container.axioms[choice]

                    display_text = BackEnd.Display.clean_axiom(axiom_id, axiom_name, actual_axiom)
                    session["data"]["display_text"] = display_text
                
                # postprocess
                if True:
                    return session

        class Settings:
            
            @staticmethod
            def on_check_verbose(session):

                if session.checkbox_verbose_logging:
                    Logger.enable = True
                    Logger.raise_error = False
                    Logger.log_level = 1000
                else:
                    Logger.enable = False

    class Display:
        
        @staticmethod
        def clean_definition(def_id: str, notation: str, actual_def: str) -> str:
            # preprocess
            if True:
                log_prefix: str = f"{BackEnd.log_prefix}[Display][clean_definition]"

            # process
            if True:
                display_text_raw: str = f"({def_id})\ {notation} ::= {actual_def}"
                display_text = display_text_raw.replace("$", "").replace(" ", "\ ")
            
            # postprocess
            if True:
                Logger.debug(f"Definition (raw): {display_text_raw}", log_prefix, 15)
                Logger.debug(f"Cleaned definition for display: {display_text}", log_prefix, 15)
                return display_text
    
        @staticmethod
        def clean_axiom(axiom_id: str, axiom_name: str, actual_axiom: str) -> str:
            # preprocess
            if True:
                log_prefix: str = f"{BackEnd.log_prefix}[Display][clean_axiom]"

            # process
            if True:
                display_text_raw: str = f"({axiom_id})\ {actual_axiom}"
                display_text = display_text_raw.replace("$", "")

                # remove "rule_xxx"
                if "rule\_" not in display_text:
                    Logger.warn("Axiom text should contain 'rule_' (for the HoTT grammar)", log_prefix, 5)
                else:
                    display_text = display_text.replace("rule\_", "")
            
            # postprocess
            if True:
                Logger.debug(f"Axiom (raw): {display_text_raw}", log_prefix, 15)
                Logger.debug(f"Cleaned axiom for display: {display_text}", log_prefix, 15)
                return display_text
