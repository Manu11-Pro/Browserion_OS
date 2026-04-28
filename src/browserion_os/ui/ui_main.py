import streamlit as st
from ui_home import home
from ui_terminal import terminal
from ui_web import web
from ui_wikipedia import wikipedia

if "present_app" not in st.session_state:
    st.session_state.present_app = "Home"

if "present_dir" not in st.session_state:
    st.session_state.present_dir = "Home$"

with st.sidebar:
    if st.button("Home", key= "Home_bt") == True:
        st.session_state.present_app = "Home"
    if st.button("Terminal", key= "Terminal_bt") == True:
        st.session_state.present_app = "Terminal"
    if st.button("Web", key="web_bt") == True:
        st.session_state.present_app = "Web"
    if st.button("Wikipedia", key="wikipedia_bt") == True:
        st.session_state.present_app = "Wikipedia"
    if st.button("Draw & Note", key="draw_and_note_bt") == True:
        st.session_state.present_app = "Draw & Note"
    if st.button("Calculator", key="calc_bt") == True:
        st.session_state.present_app = "Calc"
    if st.button("App Menu", key="app_menu_bt") == True:
        st.session_state.present_app = "App Menu"

if st.session_state.present_app == "Home":
    home()

if st.session_state.present_app == "Terminal":
    terminal()

if st.session_state.present_app == "Web":
    web()

if st.session_state.present_app == "Wikipedia":
    wikipedia()