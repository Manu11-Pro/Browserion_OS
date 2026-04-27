import streamlit as st

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
    st.date_input(label=" ", value="today")

elif st.session_state.present_app == "Web":
    st.expander(label="Web Browser", icon="🌐", width="stretch")
    st.markdown(
        """
            <html>
                <iframe src="https://www.duckduckgo.com", class="embedded_web"></iframe>
                <form action="https://duckduckgo.com/" method="GET" target="_blank">
                    <input type="text" name="q" placeholder="Search DuckDuckGo...">
                    <button type="submit">Search</button>
                </form>
            </html>
            <style>
                .embedded_web{
                    width = 250px;
                    height = 500px;
                }
            </style>
        """, unsafe_allow_html=True
    )

elif st.session_state.present_app == "Wikipedia":
    with st.expander(label="Wikipedia", icon="📖", expanded=True):
        st.markdown(
            """
                <html>
                    <iframe src="https://www.wikipedia.org/", class="embedded_web"></iframe>
                </html>
                <style>
                    .embedded_web{
                        width:100vh;
                        height:100vh;
                    }
                </style>
            """, unsafe_allow_html=True
        )

elif st.session_state.present_app == "Terminal":
    with st.expander("Terminal", key="Terminal_exp"):
        st.markdown("Welcome to Browserion Terminal")
        with st.form("Welcome to Browserion Terminal"):
            terminal_input = st.text_input(label="Terminal@DefaultUser$", value="", placeholder=f"{st.session_state.get("present_dir")}", key="cmd")
            st.markdown(terminal_input)

            if terminal_input == "cd Work":
                dir = "Work$"