########################################
#                                      #
#       Front end of the main app      #
#                                      #
########################################

import sys
import streamlit as st
import pandas
import numpy
import time
import matplotlib.pyplot as plt

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

        col1_container_select, col2_container_select = st.columns(2)
        with col1_container_select:
            def on_click_parse_latex():
                st.session_state = be.Listener.Chapters.on_parse_latex(st.session_state)
            st.button(label="parse latex file", on_click=on_click_parse_latex)
        with col2_container_select:
            def on_click_change_container():
                st.session_state = be.Listener.Chapters.on_change_container(st.session_state)
            st.selectbox(label="select math container", 
                         key="selectbox_math_container", 
                         options=st.session_state["data"]["loaded_math_containers"].keys(),
                         on_change=on_click_change_container)

    # --------------------------------------------- display maths container

    tab_doc, tab_example = st.tabs(["Document", "Example"])

    with tab_doc:

        choice_col, display_col = st.columns([1, 5])
        
        with choice_col:
            st.subheader("Choices")
            
            # callbacks
            def on_select_definition():
                st.session_state = be.Listener.Choices.on_select_definition(st.session_state)
            def on_select_axiom():
                st.session_state = be.Listener.Choices.on_select_axiom(st.session_state)
            def on_select_context():
                st.session_state = be.Listener.Choices.on_select_context(st.session_state)
            
            # choices
            st.selectbox(label="definitions",
                         key="selectbox_definition",
                         options=st.session_state["data"]["definition_choices"].keys(),
                         on_change=on_select_definition)
            st.selectbox(label="axioms",
                         key="selectbox_axioms",
                         options=st.session_state["data"]["axiom_choices"].keys(),
                         on_change=on_select_axiom)
            st.selectbox(label="contexts",
                         key="selectbox_contexts",
                         options=st.session_state["data"]["context_choices"].keys(),
                         on_change=on_select_context)
        
        with display_col:
            st.subheader("Display")
        
            st.latex(st.session_state["data"]["display_text"])

            # callbacks
            def on_click_get_ast():
                st.session_state = be.Listener.Other.on_click_get_ast(st.session_state)
            def on_click_get_derivation():
                st.session_state = be.Listener.Other.on_click_get_derivation(st.session_state)

            # buttons
            col_ast, col_derivation = st.columns(2)
            with col_ast:
                st.button("Get ast", on_click=on_click_get_ast)
            with col_derivation:
                st.button("Get derivation", on_click=on_click_get_derivation)

            st.text(st.session_state["data"]["ast_as_text"])
    
    with tab_example:
        
        st.title("Real-time Mathematical Animations")

        animation_type = st.selectbox("Animation type", ["Rotating Sine", "Growing Circle", "Particle Motion"])
        duration = st.slider("Animation duration (seconds)", 5, 30, 10)


        if st.button("Start Animation"):
            progress_bar = st.progress(0)
            plot_placeholder = st.empty()
            
            start_time = time.time()
            current_time = 0
            
            while current_time < duration:
                current_time = time.time() - start_time
                progress = min([1, current_time / duration])
                progress_bar.progress(progress)
                
                fig, ax = plt.subplots(figsize=(10, 6))
                
                if animation_type == "Rotating Sine":
                    x = numpy.linspace(0, 4*numpy.pi, 1000)
                    phase = current_time * 2 * numpy.pi
                    y = numpy.sin(x + phase)
                    ax.plot(x, y, 'b-', linewidth=2)
                    ax.set_ylim(-1.5, 1.5)
                    
                elif animation_type == "Growing Circle":
                    theta = numpy.linspace(0, 2*numpy.pi, 100)
                    radius = 1 + 0.5 * numpy.sin(current_time * 2 * numpy.pi)
                    x = radius * numpy.cos(theta)
                    y = radius * numpy.sin(theta)
                    ax.plot(x, y, 'r-', linewidth=2)
                    ax.set_xlim(-2, 2)
                    ax.set_ylim(-2, 2)
                    
                else:
                    t = numpy.linspace(0, current_time/10, 1000)
                    x = numpy.cos(2 * numpy.pi * t)
                    y = numpy.sin(3 * numpy.pi * t)
                    ax.plot(x, y, 'g-', alpha=0.7)
                    ax.plot(x[-1], y[-1], 'ro', markersize=10)
                    ax.set_xlim(-1.5, 1.5)
                    ax.set_ylim(-1.5, 1.5)
                
                ax.grid(True, alpha=0.3)
                ax.set_aspect('equal', adjustable='box')
                plot_placeholder.pyplot(fig)
                plt.close(fig)
                
                time.sleep(0.02)

        st.text("Nothing yet")
        

if __name__=="__main__":
    run()
