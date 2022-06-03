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
            excel_file = 'POSTO 2022.xlsx'
            sheet_name = '2022 Report'
            report2022 = pd.read_excel(excel_file,
                      sheet_name = sheet_name,
                      usecols = 'A:G',
                      nrows = 16)
            return report2022
    report2022 = get_data_from_excel()    

    total_cash = (report2022["Cash"].sum())
    total_cards = (report2022["Tarjetas"].sum())
    total_sales = (report2022["Total"].sum())
    average_sales = total_sales / report2022['Cobrado'].sum()
    average_per_day = total_sales/ report2022['Days Worked'].sum()
    expenses = (report2022["Expenses"].sum())

    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:
        st.subheader("Cash:")
        st.subheader(f"${total_cash:,.2f}")
        cashmetric = ((20187.96/ total_cash) * 100)   # Using Up or down trend percentage formula to determine the different in results compared to last years
        metricresult = f"{100 - cashmetric:,.2f}%"  
        col1.metric(label = '', value = '', delta = metricresult)  
        col1.metric(label = '', value = '', delta = f"${total_cash - 20187.96:,.2f}")  
    with col2:
        st.subheader("Cards:")
        st.subheader(f"${total_cards:,.2f}")
        cardmetric = ((13644.68 / total_cards) * 100)
        metricresultcard = f"{100 - cardmetric:,.2f}%"
        col2.metric(label = '', value = '', delta = metricresultcard)
        col2.metric(label = '', value = '', delta = f"${total_cards - 13644.68:,.2f}")    
    with col3:
        st.subheader("Per Day:") 
        st.subheader(f"${average_per_day:,.2f}")   
        perdaymetric = ((275.925/ average_per_day) * 100)
        metricresultperday = f"{100 - perdaymetric:,.2f}%"
        col3.metric(label = '', value = '', delta = metricresultperday)
        col3.metric(label = '', value = '', delta = f"${average_per_day - 275.925:,.2f}")
    with col4:
        st.subheader("Per Bill:")
        st.subheader(f"${average_sales:,.2f}")
        averagemetric = ((17.798 / average_sales) * 100)
        metricresultaverage = f"{100 - averagemetric:,.2f}%"
        col4.metric(label = '', value = '', delta = metricresultaverage)
        col4.metric(label = '', value = '', delta = f"${average_sales - 17.798:,.2f}")    
    with col5:
        st.subheader("Expenses:")
        st.subheader(f"${expenses:,.2f}")
        expensesmetric = ((14965.66 / expenses) * 100)
        metricresultexpenses = f"{100 - expensesmetric:,.2f}%"
        col5.metric(label = '', value = '', delta = metricresultexpenses, delta_color = "inverse") 
        col5.metric(label = '', value = '', delta = f"${expenses - 14965.66:,.2f}", delta_color = "inverse")    
    with col6:
        st.subheader("Total Sales:")
        st.subheader(f"${total_sales:,.2f}")
        totalmetric = ((33875.65 / total_sales) * 100)
        metricresulttotal = f"{100 - totalmetric:,.2f}%"
        col6.metric(label = '', value = '', delta = metricresulttotal) 
        col6.metric(label = '', value = '', delta = f"${total_sales - 33875.65:,.2f}")
    st.markdown("*The metrics demonstrate the change in performance compared to 2021's stats*")    
    st.markdown("---")

    @st.experimental_memo
    def get_data_from_excel():    
        excel_file = 'POSTO 2022.xlsx'
        sheet_name = 'EXPENSES'
        df = pd.read_excel(excel_file,
                  sheet_name = sheet_name,
                  usecols = 'A : C',
                  nrows = 16)
        return df
    df = get_data_from_excel()  

    col7, col8 = st.columns(2)
    with col8:
        fig0 = go.Scatter(
        x = df["Fecha"],
        y = df.Expenses1,
        mode = 'markers+lines',
        name = '2021 Expenses',
        marker = dict( color= 'red')
        )
        fig2 = go.Scatter(
        x = df["Fecha"],
        y = df.Expenses,
        mode = 'markers+lines',
        name = '2022 Expenses', 
        marker = dict( color= 'green')
        )
        data = [fig0, fig2]  ## Created an array to joint both figures in one table
        layout = go.Layout(title = 'Expenses 2021 Vs 2022', 
                            plot_bgcolor='rgba(0,0,0,0)', # plot_bgcolor will remove the background
                            font=dict(
                            family="Courier New, monospace",
                            size=15,
                            color="white")
                            ) 
        figure = go.Figure(data = data, layout = layout)
        figure.for_each_yaxis(lambda y: y.update(showgrid=False)) # This will delete the grid for y axis
        st.plotly_chart(figure)

    with col7:
        @st.experimental_memo
        def get_data_from_excel():    
            excel_file = 'POSTO 2022.xlsx'
            sheet_name = 'EXPENSES'
            df = pd.read_excel(excel_file,
                      sheet_name = sheet_name,
                      usecols = 'A : G',
                      nrows = 16)
            return df
        df = get_data_from_excel()  

        fig3 = go.Bar(
        x = df["Fecha1"],
        y = df.Sales1,
        name = '2021 Sales',
        marker = dict( color= 'red')
        )
        fig4 = go.Bar(
        x = df["Fecha1"],
        y = df.Sales,
        name = '2022 Sales', 
        marker = dict( color= 'green')
        )
        
        data = [fig3, fig4]  ## Created an array to joint both figures in one table
        layout = go.Layout(title = 'Sales 2021 Vs 2022', 
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
        excel_file = 'POSTO 2022.xlsx'
        sheet_name = 'WineAnalysis'
        wine = pd.read_excel(excel_file,
                  sheet_name = sheet_name,
                  usecols = 'A : C',
                  nrows = 16)
        return wine
    wine = get_data_from_excel()

    col7, col8 = st.columns(2)
    with col8:  
        with st.container():        
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
            figure.for_each_yaxis(lambda y: y.update(showgrid=False)) # This will delete the grid for y axi

            st.plotly_chart(figure)
            cantidad_vendida = (wine['Sales'].sum())
            wine_expenses = (wine['Expenses'].sum())
            st.markdown(f"Wine Sales: ${cantidad_vendida:,.2f}" " " "---" f" Wine Expenses: {wine_expenses}")
        

    @st.experimental_memo
    def get_data_from_excel():    
        excel_file = 'POSTO 2022.xlsx'
        sheet_name = 'EXPENSES'
        df = pd.read_excel(excel_file,
                  sheet_name = sheet_name,
                  usecols = 'A : G',
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


