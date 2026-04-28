import streamlit as st

def wikipedia():
    with st.expander(label="Wikipedia", icon="📖", expanded=True):
        st.iframe("https://wikipedia.org", height=600)