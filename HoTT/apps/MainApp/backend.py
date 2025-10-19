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
                "definition_choices": [],
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
                    log_prefix: str = f"{BackEnd.log_prefix}[Listener][on_parse_latex]"
                    container: MathContainer = st.session_state["data"]["math_container"]
                    definitions: Dict[str, str] = container.definitions
                    choices = []
                
                # process
                if len(definitions) > 0:
                    choices = list(definitions.keys())

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
                    definition_choices = BackEnd.Get.Choices.definition_choices(st.session_state)
                    session["data"]["definition_choices"] = definition_choices
                    Logger.debug(f"Definition choices: {definition_choices}", log_prefix, 5)

                # postprocess
                if True:
                    return session
        
        class Choices:

            @staticmethod
            def on_select_definition(session):

                # preprocess
                if True:
                    log_prefix: str = f"{BackEnd.log_prefix}[Listener][on_select_definition]"

                    container = session["data"]["math_container"]
                    choice = session["selectbox_definition"]

                # process
                if True:
                    def_id, notation = choice.split(":::")
                    Logger.debug(f"Chosen definition: id={def_id}, notation={notation}", log_prefix, 5)
                    actual_def = container.definitions[choice]

                    session["data"]["display_text"] = f"({def_id}) {notation} ::= {actual_def}"
                
                # postprocess
                if True:
                    return session
        
        class Display:
            
            pass
        
        class Settings:
            
            @staticmethod
            def on_check_verbose(session):

                if session.checkbox_verbose_logging:
                    Logger.enable = True
                    Logger.raise_error = False
                    Logger.log_level = 1000
                else:
                    Logger.enable = False
