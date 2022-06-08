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

    @st.experimental_memo
    def get_data_from_excel():    
            excel_file = 'POSTO SALES.xlsx'
            sheet_name = '2021 Report'
            report2021 = pd.read_excel(excel_file,
                      sheet_name = sheet_name,
                      usecols = 'A:G',
                      nrows = 16)
            return report2021
    report2021 = get_data_from_excel()    

    total_cash = (report2021["Cash"].sum()) # Getting the sum for each column from the dataframe
    total_cards = (report2021["Tarjetas"].sum())  # Same logic is applied to the rest
    total_sales = (report2021["Total"].sum())
    average_sales = total_sales / report2021['Cobrado'].sum() # Getting the average sale per bill by diving the total by how many receipts we got
    average_per_day = total_sales/ report2021['Days Worked'].sum() # The average per day is calculate by the total sales to the amount of days worked
    expenses = (report2021["Expenses"].sum())

    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:
        st.subheader("Cash:")
        st.subheader(f"${total_cash:,.2f}")
    with col2:
        st.subheader("Cards:")
        st.subheader(f"${total_cards:,.2f}") 
    with col3:
        st.subheader("Per Day:") 
        st.subheader(f"${average_per_day:,.2f}")   
    with col4:
        st.subheader("Per Bill:")
        st.subheader(f"${average_sales:,.2f}")    
    with col5:
        st.subheader("Expenses:")
        st.subheader(f"${expenses:,.2f}")  
    with col6:
        st.subheader("Total Sales:")
        st.subheader(f"${total_sales:,.2f}")
    st.markdown("---")  


    col6, col7 = st.columns(2)

    @st.experimental_memo
    def get_data_from_excel():    
            excel_file = 'POSTO SALES.xlsx'
            sheet_name = 'HOURS'
            df = pd.read_excel(excel_file,
                      sheet_name = sheet_name,
                      usecols = 'A:B',
                      nrows = 16)
            return df
    df = get_data_from_excel()

    with col6:

        fig = go.Figure(
            data=[go.Scatter(y = df["Total"], x = df['Hora'])],
        )
        fig.update_traces(line_color = "green")

        fig.update_layout(
        title="Total Sold Per Hour",
        xaxis_title="Hour",
        yaxis_title="Total",
        font=dict(
            family="Courier New, monospace",
            size=15,
            color="white"
        ), 
        plot_bgcolor='rgba(0,0,0,0)' ## plot_bgcolor will remove background color
    )
        fig.for_each_xaxis(lambda x: x.update(showgrid=False))  # This will delete the grid for both x and y axis
        fig.for_each_yaxis(lambda y: y.update(showgrid=False))
        st.plotly_chart(fig)

 

    @st.experimental_memo
    def get_data_from_excel():    
        excel_file = 'POSTO SALES.xlsx'
        sheet_name = 'EXPENSES'
        df = pd.read_excel(excel_file,
                  sheet_name = sheet_name,
                  usecols = 'A : C',
                  nrows = 16)
        return df
    df = get_data_from_excel()  
    
    with col7:
        fig0 = go.Bar(
        x = df["Fecha"],
        y = df.Sales,
        name = 'Sales',
        marker = dict( color= 'green')

        )


        fig2 = go.Scatter(
        x = df["Fecha"],
        y = df.Expenses,
        mode = 'markers+lines',
        name = 'Expenses', 
        marker = dict( color= 'red')
        )

        data = [fig0, fig2]  ## Created an array to joint both figures in one table

        layout = go.Layout(title = 'Expenses Vs Sales', 
                            plot_bgcolor='rgba(0,0,0,0)', # plot_bgcolor will remove the background
                            font=dict(
                            family="Courier New, monospace",
                            size=15,
                            color="white")
                            ) 

        figure = go.Figure(data = data, layout = layout)
        figure.for_each_yaxis(lambda y: y.update(showgrid=False)) # This will delete the grid for y axis

        st.plotly_chart(figure)
    st.markdown("---")

    @st.experimental_memo
    def get_data_from_excel():    
        excel_file = 'POSTO SALES.xlsx'
        sheet_name = 'Sub Categories'
        df3 = pd.read_excel(excel_file,
                  sheet_name = sheet_name,
                  usecols = 'A : S',
                  nrows = 79)
        return df3
    df3 = get_data_from_excel()  

    col1, col2 = st.columns(2)

    with col1:

        productlist = df3["Producto"].unique().tolist()

        product = st.multiselect("Select Product to Analyze Sales Per Hour", productlist)

        dfs = {product: df3[df3["Producto"] == product] for product in product}

        fig3 = go.Figure()
        for product, df3 in dfs.items():
            fig3 = fig3.add_trace(go.Scatter(x=df3["Hora"], y = df3["Valor"], name = product))
            fig3.for_each_yaxis(lambda y: y.update(showgrid=False))
            fig3.for_each_xaxis(lambda x: x.update(showgrid=False))
            fig3.update_layout(
            font=dict(
            family="Courier New, monospace",
            size=15,
            color="white"
        ), plot_bgcolor='rgba(0,0,0,0)')

        st.plotly_chart(fig3)

    with col2:
        @st.experimental_memo
        def get_data_from_excel():    
            excel_file = 'POSTO SALES.xlsx'
            sheet_name = 'WinesAnalysis'
            wine = pd.read_excel(excel_file,
                      sheet_name = sheet_name,
                      usecols = 'A : C',
                      nrows = 16)
            return wine
        wine = get_data_from_excel()  
        
        sales = go.Bar(
        x = wine["Fecha"],
        y = wine.Sales,
        name = 'Sales',
        marker = dict( color= 'violet')

        )
        expenses = go.Scatter(
        x = wine["Fecha"],
        y = wine.Expenses,
        mode = 'markers+lines',
        name = 'Expenses', 
        marker = dict( color= 'red')
        )

        data = [sales, expenses]  ## Created an array to joint both figures in one table

        layout = go.Layout(title = 'Wine Expenses Vs Wine Sales', 
                            plot_bgcolor='rgba(0,0,0,0)', # plot_bgcolor will remove the background
                            font=dict(
                            family="Courier New, monospace",
                            size=15,
                            color="white")
                            ) 

        figure = go.Figure(data = data, layout = layout)
        figure.for_each_yaxis(lambda y: y.update(showgrid=False)) # This will delete the grid for y axis

        st.plotly_chart(figure)
    st.markdown("---")