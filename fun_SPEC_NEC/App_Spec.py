# import streamlit as st

# # --- Page Setup ---

# about_Me = st.Page(
#     page = 'about_me.py',
#     title = "About Me",
# )

# project_1_page = st.Page(
#     page = 'SpecNec_executable_streamlit.py',
#     title = "Spec NEC",
#     default= True,
# )

# ## --- Navigation

# pg = st.navigation(
#     {
#         "info": [about_Me],
#         "Basic Apps": [project_1_page],
#     }
# )

# pg.run()

import streamlit as st
import runpy

def main():
    st.sidebar.title("Navigation")
    app_mode = st.sidebar.radio("Go to", ["About Me", "Spec NEC"])

    if app_mode == "About Me":
        about_me()
    elif app_mode == "Spec NEC":
        spec_nec()

def about_me():
    runpy.run_path('about_me.py')

def spec_nec():
    runpy.run_path('SpecNec_executable_streamlit.py')

if __name__ == "__main__":
    main()


