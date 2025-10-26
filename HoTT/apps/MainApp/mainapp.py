########################################
#                                      #
#       Front end of the main app      #
#                                      #
########################################

import sys
import streamlit as st
import pandas
import numpy

proj_dir = "Maths/HoTT".lower()
hott_dir = __file__[:__file__.lower().rfind(proj_dir) + len(proj_dir)]
if hott_dir not in sys.path:
    sys.path = [hott_dir] + sys.path

from apps.MainApp.backend import BackEnd as be


def init():

    st.set_page_config(layout="wide")
    
    st.session_state["data"] = be.Data.load()

    st.session_state = be.init(st.session_state)


def run():

    if "data" not in st.session_state.keys():
        init()
    
    st.title('HoTT main app')

    # --------------------------------------------- settings

    st.checkbox(label='Verbose logging', 
                value=True, 
                key="checkbox_verbose_logging",
                on_change=lambda _:be.Listener.Settings.on_check_verbose(st.session_state))

    # --------------------------------------------- chapter selection

    st.subheader('/'.join(st.session_state["data"]["selected_chapter_path"]))

    def on_select_subchapter():
        st.session_state = be.Listener.Chapters.on_select_subchapter(st.session_state)
    st.selectbox(label="Select a chapter to study", 
                 key="selectbox_subchapter",
                 options=st.session_state["data"]["subchapters"],
                 on_change=on_select_subchapter)
    def on_previous_chapter():
        st.session_state = be.Listener.Chapters.on_previous_chapter(st.session_state)
    st.button("Go to previous chapter", on_click=on_previous_chapter)

    if st.session_state["data"]["selected_chapter_tex_file"] != "":

        st.text("Latex file : " + st.session_state["data"]["selected_chapter_tex_file"])

        def on_click_parse_latex():
            st.session_state = be.Listener.Chapters.on_parse_latex(st.session_state)
        st.button(label="parse latex file", on_click=on_click_parse_latex)

    # --------------------------------------------- display maths container

    choice_col, display_col = st.columns([1, 5])
    
    with choice_col:
        st.subheader("Choices")
        
        # callbacks
        def on_select_definition():
            st.session_state = be.Listener.Choices.on_select_definition(st.session_state)
        def on_select_axiom():
            st.session_state = be.Listener.Choices.on_select_axiom(st.session_state)
        # choices
        st.selectbox(label="definitions",
                     key="selectbox_definition",
                     options=st.session_state["data"]["definition_choices"].keys(),
                     on_change=on_select_definition)
        st.selectbox(label="axioms",
                     key="selectbox_axioms",
                     options=st.session_state["data"]["axiom_choices"].keys(),
                     on_change=on_select_axiom)

    
    with display_col:
        st.subheader("Display")
        
        st.latex(st.session_state["data"]["display_text"])
        

if __name__=="__main__":
    run()
