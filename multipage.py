# To generate mutliple streamlit applications through an object oriented framework

import streamlit as st
from PIL import Image

from pages.Report2021 import app
from pages2.ProductAnalysis import app as app1
# from pages.January2021 import app as app2



# To manage multiple apps in the program
class Multipage:

    def __init__(self) -> None:
        # Constructor class to generate a list which will store all the applications as an instance variable
        self.pages = []
        self.pages2 = []

    def add_page(self, title, func) -> None:
        # Class method to add pages to the project

        # Args : title([str]) The title of the page that is being add to the app
        #        func: Python function to render the page in streamlit

        self.pages.append(
            {
                "title" : title,
                "function" : func
            }
        )
        self.pages2.append(
            {
                "title" : title,
                "function" : func
            }
        )

    def run(self):

        st.set_page_config(page_title= "POSTO",
                   page_icon=":pizza:" ,
                   layout="wide")
        st.image('Posto Letrero.png', use_column_width=None)

        pages = {
          "Main": "Overview Report of 2021",
          "Monthly": "Monthly Reports of 2021"
        }
        st.sidebar.markdown("## Data Visualization of 2021")
        selected_page = st.sidebar.radio("", pages.values())

        if selected_page == pages["Main"]:  
            pages={'title': '', 'function': app }
            pages2={'title': '', 'function': app1 }
            
            pages['function']()
            pages2['function']()

        elif selected_page == pages['Monthly']:    
            pages = st.sidebar.selectbox(
            'Reports', 
            self.pages,
            format_func=lambda page: page['title']
        )
        
            pages['function']()