#######################################
#                                     #
#       Back end of the main app      #
#                                     #
#######################################

import sys
import os
import traceback
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
from src.Parsing.Grammar.hott_parser import HottParser
from src.Parsing.LaTeX.latex_parser import LatexTransformer


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
                "loaded_math_containers": {},
                # choices and display
                "definition_choices": {},
                "axiom_choices": {},
                "context_choices": {},
                "text_for_ast": "",
                "ast_as_text": "",
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

            @staticmethod
            def context_choices(session) -> list[str]:
                # preprocess
                if True:
                    log_prefix: str = f"{BackEnd.log_prefix}[Listener][context_choices]"
                    container: MathContainer = st.session_state["data"]["math_container"]
                    contexts: Dict[str, str] = container.contexts
                    choices = []
                
                # process
                if len(contexts) > 0:
                    choices = list(contexts.keys())

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
                    session["data"]["loaded_math_containers"][file] = container
                    
                    session = BackEnd.Listener.Choices.update_choices(session, container)

                # postprocess
                if True:
                    return session

            @staticmethod
            def on_change_container(session):
                
                # preprocess
                if True:
                    log_prefix: str = f"{BackEnd.log_prefix}[Listener][on_change_container]"
                    file: str = st.session_state["selectbox_math_container"]
                
                # process
                if True:
                    if file not in session["data"]["loaded_math_containers"].keys():
                        Logger.error(
                            f"Wrong container selected ({file}). Available containers : " +\
                            f"{session['data']['loaded_math_containers'].keys()}", 
                            log_prefix, 
                            5)
                        return session
                    container = session["data"]["loaded_math_containers"][file]
                    session["data"]["math_container"] = container
                    session["data"]["loaded_math_containers"][file] = container
                    
                    session = BackEnd.Listener.Choices.update_choices(session, container)

                # postprocess
                if True:
                    return session
       
        class Choices:
        
            def update_choices(session, container: MathContainer):
                
                # preprocess
                if True:
                    log_prefix: str = f"{BackEnd.log_prefix}[Listener][update_choices]"
                    file: str = st.session_state["selectbox_math_container"]
                
                # process
                if True:
                    
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
                    # contexts
                    if True:
                        context_choices_raw = BackEnd.Get.Choices.context_choices(st.session_state)
                        context_choices_clean = [a.replace(":::", ":").replace("$", "") for a in context_choices_raw]
                        context_choices_display = {a1: a2 for a1, a2 in zip(context_choices_clean, context_choices_raw)}
                        session["data"]["context_choices"] = context_choices_display

                # postprocess
                if True:
                    Logger.debug(f"Definition choices: {def_choices_clean}", log_prefix, 5)
                    Logger.debug(f"Axiom choices: {axiom_choices_clean}", log_prefix, 5)
                    Logger.debug(f"Context choices: {context_choices_clean}", log_prefix, 5)
                    return session

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
                    session = BackEnd.Listener.Choices.update_display_zone(session, display_text, "")
                
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
                    session = BackEnd.Listener.Choices.update_display_zone(session, display_text, actual_axiom)

                # postprocess
                if True:
                    return session

            @staticmethod
            def on_select_context(session):

                # preprocess
                if True:
                    log_prefix: str = f"{BackEnd.log_prefix}[Listener][on_select_context]"

                    container = session["data"]["math_container"]
                    choice_displayed = session["selectbox_contexts"]
                    choice = session["data"]["context_choices"][choice_displayed]

                # process
                if True:
                    context_id, context_name = choice.split(":::")
                    context_id = context_id.replace(" ", "")
                    Logger.debug(f"Chosen context: id={context_id}, context name={context_name}", log_prefix, 5)
                    actual_context = container.contexts[choice]

                    display_text = BackEnd.Display.clean_context(context_id, context_name, actual_context)
                    session = BackEnd.Listener.Choices.update_display_zone(session, display_text, actual_context)

                # postprocess
                if True:
                    return session

            @staticmethod
            def update_display_zone(session, display_text, text_for_ast):

                # preprocess
                if True:
                    log_prefix: str = f"{BackEnd.log_prefix}[Listener][update_display_zone]"

                # process
                if True:
                    session["data"]["display_text"] = str(display_text)
                    session["data"]["text_for_ast"] = str(text_for_ast)
                    session["data"]["ast_as_text"] = ""

                # postprocess
                if True:
                    return session

        class Other:
            
            @staticmethod
            def on_click_get_ast(session):
                
                # preprocess
                if True:
                    log_prefix: str = f"{BackEnd.log_prefix}[Listener][on_click_get_ast]"

                    text_for_ast = session["data"]["text_for_ast"]
                    #container = session["data"]["math_container"]

                # process
                if text_for_ast != "":

                    text_for_ast = text_for_ast.replace("$", "").replace("\\_", "_")\
                        .replace("\\text{——}", "—————").replace("\\ ", " ").replace("\\vdash", "⊢")
                    text_for_ast = LatexTransformer.replace_all_commands(text_for_ast)
                    Logger.debug(f"Text for ast : {text_for_ast}", log_prefix)
                    
                    try:
                        parsed = HottParser.get_HoTT_tree(text_for_ast, "inference_system")
                        session["data"]["ast_as_text"] = parsed.pretty()
                    except Exception as e:
                        session["data"]["ast_as_text"] = f"Couldn't parse. Error: {traceback.format_exc()}"

                
                # postprocess
                if True:
                    return session

            @staticmethod
            def on_click_get_derivation(session):
                
                # preprocess
                if True:
                    log_prefix: str = f"{BackEnd.log_prefix}[Listener][on_click_get_derivation]"

                    text_for_derivation = session["data"]["text_for_ast"]
                    inferences = text_for_derivation.replace("\\_", "_").split("\n")
                    Logger.debug(f"Text for derivation : {inferences}", log_prefix)                    

                # process
                if text_for_derivation != "":

                    inferences_retrieved = []
                    for inference in inferences:
                        try:
                            inference_type, inference_retrieved = LatexToUI.retrieve_derivation(
                                inference, 
                                session["data"]["loaded_math_containers"]
                            )

                            if inference_type is None:
                                session["data"]["ast_as_text"] = f"Couldn't get inference {inference}"
                                Logger.error(session["data"]["ast_as_text"], log_prefix) 
                                return session

                            inference_id = inference.split(" -> ")[1]
                            inferences_retrieved.append((inference_id, inference_type, inference_retrieved))
                        except Exception as e:
                            session["data"]["ast_as_text"] = f"Couldn't get inference {inference}. Error: {traceback.format_exc()}"
                            Logger.error(session["data"]["ast_as_text"], log_prefix)
                            return session
               
                # postprocess
                if True:
                    text_for_ast = '\n'.join([el[1] for el in inferences_retrieved])

                    display_texts = []
                    for inference_id, inference_type, inference_retrieved in inferences_retrieved:

                        display_text = f"({inference_id}) : \\text{{None}}"
                        if inference_type == "axiom_apply":
                            display_text = BackEnd.Display.clean_axiom(inference_id, "", inference_retrieved)
                        
                        display_texts.append(display_text)
                    
                    display_text = '\\\\'.join(display_texts)

                    session = BackEnd.Listener.Choices.on_select_context(session)
                    current_text = session["data"]["display_text"]
                    display_text = f"{current_text} \\\\~\\\\ {display_text}"
                    
                    Logger.debug(f"Retrieved derivations : {display_text}", log_prefix, 6)                    
                    session = BackEnd.Listener.Choices.update_display_zone(session, display_text, text_for_ast)
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
        def clean_common(text):
            
            text = text.replace("context\\_", "").replace("var\\_", "")\
                .replace("Type\\_", "\\mathcal{U}_").replace("pair(", "(")\
                .replace("empty_type", "0").replace("unit_type", "1")\
                .replace("name\\_", "").replace("\\Id", "Id").replace("refl\\_", "refl_")
            
            return text

        @staticmethod
        def clean_definition(def_id: str, notation: str, actual_def: str) -> str:
            # preprocess
            if True:
                log_prefix: str = f"{BackEnd.log_prefix}[Display][clean_definition]"

            # process
            if True:
                display_text_raw: str = f"({def_id})\\ {notation} ::= {actual_def}"
                display_text = display_text_raw.replace("$", "").replace(" ", "\\ ")
                display_text = LatexTransformer.replace_all_commands(display_text)
                display_text = BackEnd.Display.clean_common(display_text)
            
            # postprocess
            if True:
                Logger.debug(f"Definition (raw): {display_text_raw}", log_prefix, 15)
                Logger.debug(f"Cleaned definition for display: {display_text}", log_prefix, 15)
                return display_text
    
        @staticmethod
        def clean_context(context_id: str, context_name: str, actual_context: str) -> str:
            # preprocess
            if True:
                log_prefix: str = f"{BackEnd.log_prefix}[Display][clean_context]"

            # process
            if True:
                display_text_raw: str = f"({context_id})\ {actual_context}"
                display_text = display_text_raw.replace("$", "")
                display_text = LatexTransformer.replace_all_commands(display_text)
                display_text = BackEnd.Display.clean_common(display_text)

            # postprocess
            if True:
                Logger.debug(f"Context (raw): {display_text_raw}", log_prefix, 15)
                Logger.debug(f"Cleaned context for display: {display_text}", log_prefix, 15)
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
                display_text = LatexTransformer.replace_all_commands(display_text)
                display_text = BackEnd.Display.clean_common(display_text)

                # remove "rule_xxx"
                if "rule\\_" not in display_text:
                    Logger.warn("Axiom text should contain 'rule_' (for the HoTT grammar)", log_prefix, 5)
                else:
                    display_text = display_text.replace("rule\\_", "").replace("—————", "\\text{——}")
            
            # postprocess
            if True:
                Logger.debug(f"Axiom (raw): {display_text_raw}", log_prefix, 15)
                Logger.debug(f"Cleaned axiom for display: {display_text}", log_prefix, 15)
                return display_text
