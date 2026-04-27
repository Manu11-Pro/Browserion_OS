import streamlit as st

with st.sidebar:
    Home = st.button("Home", key= "Home_bt")
    Terminal = st.button("Terminal", key= "Terminal_bt")
    Web = st.button("Web", key="web_bt")
    Draw_and_note = st.button("Draw & Note", key="draw_and_note_bt")
    calc = st.button("Calculator", key="calc_bt")
    app_menu = st.button("App Menu", key="app_menu_bt")

if Home == True:
    st.date_input(label=" ", value="today")

if Web == True:
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

if Terminal == True:
    with st.expander("Terminal"):
        st.markdown("Welcome to Browserion Terminal")
        st.text_input(label="Terminal@DefaultUser$", value="", placeholder="--help for cmd list")

# st.markdown(
#     """
#         <html>
#             <iframe src="www.google.com">
#         </html>
#         <style?>
#             .embedded_web{ 
#             }
#         </style>
#     """
# )