import streamlit as st

# --- Page Setup ---

about_Me = st.Page(
    page = 'views/about_me.py',
    title = "About Me",
    # icon = ":material/account_circle"
)

project_1_page = st.Page(
    page = 'views/SpecNec_executable_streamlit.py',
    title = "Spec NEC",
    # icon = ":material/smart_toy",
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