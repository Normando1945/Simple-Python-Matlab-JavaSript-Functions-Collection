import streamlit as st

# --- Page Setup ---

about_Me = st.Page(
    page = 'about_me.py',
    title = "About Me",
)

project_1_page = st.Page(
    page = 'SpecNec_executable_streamlit.py',
    title = "Spec NEC",
    default= True,
)

## --- Navigation

pg = st.navigation(
    {
        "info": [about_Me],
        "Basic Apps": [project_1_page],
    }
)

pg.run()
