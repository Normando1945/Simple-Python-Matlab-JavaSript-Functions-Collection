import streamlit as st

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

# Define a simple navigation function
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["About Me", "Spec NEC"])

    if page == "About Me":
        about_me()
    elif page == "Spec NEC":
        spec_nec()

def about_me():
    st.title("About Me")
    runpy('about_me.py')

def spec_nec():
    st.title("Spec NEC")
    runpy('SpecNec_executable_streamlit.py')

def runpy(filepath):
    with open(filepath) as file:
        exec(file.read(), globals())

if __name__ == "__main__":
    main()

