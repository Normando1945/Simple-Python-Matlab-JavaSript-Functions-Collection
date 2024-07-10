import streamlit as st
# from streamlit_option_menu import option_menu

# --- Page Setup ---

about_Me = st.Page(
    page = 'pages/about_me.py',
    title = "About Me",
    icon = "😎",
    # icon = ":material/account_circle"
)

project_1_page = st.Page(
    page = 'pages/SpecNec_executable_streamlit.py',
    title = "Spec NEC",
    # icon = ":material/smart_toy",
    default= True,
)

## --- Navigation

pg = st.navigation(
    {
        "📔 info": [about_Me],
        "💻 Basic Apps": [project_1_page],
    }
)

pg.run()