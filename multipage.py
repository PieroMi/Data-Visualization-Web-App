# To generate mutliple streamlit applications through an object oriented framework

from soupsieve import select
import streamlit as st
from PIL import Image

from pages.Report2021 import app
from pages2.ProductAnalysis import app as app1
from pages3.Report2022 import app as app2
from pages3.ProductAnalysis2022 import app as app3

# To manage multiple apps in the program
class Multipage:

    def __init__(self) -> None:
        # Constructor class to generate a list which will store all the applications as an instance variable
        self.pages = []

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

    def run(self):

        st.set_page_config(page_title= "POSTO",
                   page_icon=":pizza:" ,
                   layout="wide")
        st.image('Posto Letrero.png', use_column_width=None)

        pages = {
          "2022" : "Overview Report of 2022",
          "Main": "Overview Report of 2021",
          "Monthly": "Monthly Reports"
        }

        st.sidebar.markdown('## **Data Visualization**')
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

        elif selected_page == pages['2022']:
            pages3 = {'title': '', 'function' : app2}
            pages4 = {'title': '', 'function' : app3}

            pages3['function']()
            pages4['function']()        
