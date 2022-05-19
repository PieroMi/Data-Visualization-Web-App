import os
import streamlit as st
import numpy as np
from PIL import Image
import tkinter

from multipage import Multipage
from pages import January2021, February2021, March2021, April2021, May2021, June2021, July2021, August2021, September2021, October2021, November2021, December2021
from pages2 import ProductAnalysis

app = Multipage()


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
app.add_page("test", ProductAnalysis.app)


app.run()