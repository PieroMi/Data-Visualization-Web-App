import streamlit as st
import pandas as pd
from pandas import io
from pandas.io import excel
from pandas.io.formats import style
from PIL import Image
import plotly.express as px
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
import plotly.graph_objects as go



def app():
    st.title('Hello')

    chcs1 = ((3469/5352) * 100)
    chsc2 = f"%{100 - chcs1:,.2f}"
# 

    st.markdown(chcs1)
    st.metric(label = '', value = chcs1, delta=chsc2)

