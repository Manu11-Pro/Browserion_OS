import streamlit as st

def home():
    if st.session_state.present_app == "Home":
        st.markdown("# BrowserionOS", text_alignment="center")
        st.time_input(label="", value="now", disabled=True)
        st.date_input(label="", value="today", disabled=True)