import streamlit as st
from multipage import Multipage
from pages import January2021, February2021, March2021, April2021, May2021, June2021, July2021, August2021, September2021, October2021, November2021, December2021, January2022, February2022, March2022, April2022, May2022

app = Multipage() # The instance for the app

# This class will handle the structure of the application

# Once the select box is clicked on the web app it will display all these classes
app.add_page("January 2021", January2021.app)
app.add_page("February 2021", February2021.app)
app.add_page("March 2021", March2021.app)
app.add_page("April 2021", April2021.app)
app.add_page("May 2021", May2021.app)
app.add_page("June 2021", June2021.app)
app.add_page("July 2021", July2021.app)
app.add_page("August 2021", August2021.app)
app.add_page("September 2021", September2021.app)
app.add_page("October 2021", October2021.app)
app.add_page("November 2021", November2021.app)
app.add_page("December 2021", December2021.app)
app.add_page("January 2022", January2022.app)
app.add_page("February 2022", February2022.app)
app.add_page("March 2022", March2022.app)
app.add_page("April 2022", April2022.app)
app.add_page("May 2022", May2022.app)


app.run()
