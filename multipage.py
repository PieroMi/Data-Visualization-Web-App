# To generate mutliple streamlit applications through an object oriented framework
import streamlit as st

from Report2021.report2021 import app as report2021
from ProductAnalysis2021.ProductAnalysis2021 import app as prodAnalysis2021
from Report2022.Report2022 import app as report2022
from ProductAnalysis2022.ProductAnalysis2022 import app as prodAnalysis2022

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

        st.set_page_config(page_title= "POSTO",   # Setting the page configuration so that when it loads on any page it will still display this.
                   page_icon=":pizza:" ,
                   layout="wide"
                   )
        st.image('Posto Letrero.png', use_column_width=None)

        pages = {  # An array that stores These strings and will be displayed as a radio button widget on streamlit
          "2022" : "📊Overview Report of 2022",
          "2021": "📈Overview Report of 2021",
          "Monthly": "📝Monthly Reports"
        }

        st.sidebar.markdown('## **Data Visualization**')
        selected_page = st.sidebar.radio("", pages.values())  # The radio button will return pages from above 

        if selected_page == pages["2021"]:  # A few if statements that will indicate which button in the radio widget is selected
            report={'title': '', 'function': report2021 } # If a certain button is clicked it will return the constructor class of self.pages[] 
            prodanalysis={'title': '', 'function': prodAnalysis2021 } # And return whichever class is in the if statement
            # It is returning two pages for '2021' the report and the in depth analysis of the products 

            #This will run the application 
            report['function']()
            prodanalysis['function']()

        elif selected_page == pages['Monthly']:    # This if statement will return a selectbox widget with all the pages available from Multipage 
            pages = st.sidebar.selectbox(
            'Reports', 
            self.pages,
            format_func=lambda page: page['title']
        )
            pages['function']()

        elif selected_page == pages['2022']:
            report22 = {'title': '', 'function' : report2022}
            analysis22 = {'title': '', 'function' : prodAnalysis2022}

            report22['function']()
            analysis22['function']()        