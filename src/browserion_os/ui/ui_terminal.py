import streamlit as st

def terminal():
    with st.expander("Terminal", key="Terminal_exp", expanded=True):
        st.markdown("Welcome to Browserion Terminal")
        with st.form("Welcome to Browserion Terminal"):
            terminal_input = st.text_input(label="Terminal@DefaultUser$", value="", placeholder=f"{st.session_state.get("present_dir")}", key="cmd")
            st.form_submit_button(label="Submit")
            st.markdown(terminal_input)

            st.text_area(label="Cmds")