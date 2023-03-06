from tkinter import font
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


excel_file = 'POSTO SALES.xlsx' 

def app():
    @st.cache_data   # Cache
    def get_data_from_excel():    
        excel_file = 'POSTO SALES.xlsx'
        sheet_name = 'SLICES'
        df = pd.read_excel(excel_file,
                          sheet_name = sheet_name,
                          usecols = 'A:D',
                          nrows = 197)
        return df
    df = get_data_from_excel()

    product = ['', 'Slices', 'Pizzas', 'Drinks', 'Wines', 'Beers', 'Sweets & Others'] # A dict that is represented by a variable 
    select_product = st.sidebar.selectbox("Select A Category To Analyze its Performance", product) # That variable is used in the selectbox widget

    if select_product == 'Slices':


        producto = st.sidebar.multiselect("Select the Product:", # The multiselect widget returns a list of strings that contain the selected options
                                   options= df["Producto"].unique(), # Returns the product name from the producto column
                                   default= df["Producto"].unique()  
                                   )
        Hora = st.sidebar.multiselect("Select the Hour:",
                                   options= df["Hora"].unique(),
                                   default= df["Hora"].unique()
                                   )

        df_selection = df.query( # Will query all the columns 
                                "Producto == @producto & Hora == @Hora"
        )
        col1, col2, col3 = st.columns(3)
        with col1:
            cantidad_vendida = (df_selection['Cantidad'].sum()) # Because we queried Product and Hour to 1 variable it allows me to gather the total quantity sold per product and per hour
            st.subheader(f"Products sold: {cantidad_vendida:,.2f}")  
        with col2:
            valor_vendida = (df_selection['Valor'].sum()) 
            st.subheader(f"Total Sold: ${valor_vendida:,.2f}")  
        with col3:
            promedio_vendida = (valor_vendida / cantidad_vendida) 
            st.subheader(f"Average Sold: ${promedio_vendida:,.2f}")  

        col4, col5 = st.columns(2)
        with col4:
            bar_chart = px.bar(df_selection,
                               x = 'Hora',
                               y = 'Cantidad',
                               color = 'Producto',
                               )

            bar_chart.update_layout(
                font=dict(
                family="Courier New, monospace",
                size=15,
                color="white"
            )
            )

            bar_chart.for_each_xaxis(lambda x: x.update(showgrid=False))  # This will delete the grid for both x and y axis   
            st.plotly_chart(bar_chart)

        with col5:
            all_products_sold = df_selection.groupby(by=["Producto"]).sum()[["Cantidad"]]
 
            products_sold = px.pie(
            all_products_sold,
            values = 'Cantidad',
            names = all_products_sold.index
            )
            products_sold.update_layout(height = 500, showlegend= False)
            products_sold.update_traces(textposition = 'inside', textinfo = 'percent+label', hole = .3)            
            st.plotly_chart(products_sold) 


    if select_product == 'Drinks':

        @st.cache_data
        def get_data_from_excel():    
                excel_file = 'POSTO SALES.xlsx'
                sheet_name = 'DRINKS'
                df = pd.read_excel(excel_file,
                          sheet_name = sheet_name,
                          usecols = 'A:D',
                          nrows = 235)
                return df
        df = get_data_from_excel()


        producto = st.sidebar.multiselect("Select the Product:",
                                   options= df["Producto"].unique(),
                                   default= df["Producto"].unique()
                                   )
        Hora = st.sidebar.multiselect("Select the Hour:",
                                   options= df["Hora"].unique(),
                                   default= df["Hora"].unique()
                                   )
        df_selection = df.query(
                                "Producto == @producto & Hora == @Hora"
        )

        col1, col2, col3 = st.columns(3)
        with col1:
            cantidad_vendida = (df_selection['Cantidad'].sum()) 
            st.subheader(f"Products sold: {cantidad_vendida:,.2f}")  
        with col2:
            valor_vendida = (df_selection['Valor'].sum()) 
            st.subheader(f"Total Sold: ${valor_vendida:,.2f}")  
        with col3:
            promedio_vendida = (valor_vendida / cantidad_vendida) 
            st.subheader(f"Average Sold: ${promedio_vendida:,.2f}")  

        col4, col5 = st.columns(2)
        with col4:
            bar_chart = px.bar(df_selection,
                               x = 'Hora',
                               y = 'Cantidad',
                               color = 'Producto',
                               )

            bar_chart.update_layout(
                font=dict(
                family="Courier New, monospace",
                size=15,
                color="white"
            )
            )

            bar_chart.for_each_xaxis(lambda x: x.update(showgrid=False))  # This will delete the grid for both x and y axis   
            st.plotly_chart(bar_chart)

        with col5:
            all_products_sold = df_selection.groupby(by=["Producto"]).sum()[["Cantidad"]]
 
            products_sold = px.pie(
            all_products_sold,
            values = 'Cantidad',
            names = all_products_sold.index
            )
            products_sold.update_layout(height = 500, showlegend= False)
            products_sold.update_traces(textposition = 'inside', textinfo = 'percent+label', hole = .3)            
            st.plotly_chart(products_sold) 

    if select_product == 'Pizzas':

        @st.cache_data
        def get_data_from_excel():    
                excel_file = 'POSTO SALES.xlsx'
                sheet_name = 'PIZZAS'
                df = pd.read_excel(excel_file,
                          sheet_name = sheet_name,
                          usecols = 'A:D',
                          nrows = 223)
                return df
        df = get_data_from_excel()
# 

        producto = st.sidebar.multiselect("Select the Product:",
                                   options= df["Producto"].unique(),
                                   default= df["Producto"].unique()
                                   )
        Hora = st.sidebar.multiselect("Select the Hour:",
                                   options= df["Hora"].unique(),
                                   default= df["Hora"].unique()
                                   )
        df_selection = df.query(
                                "Producto == @producto & Hora == @Hora", 

        )
        col1, col2, col3 = st.columns(3)
        with col1:
            cantidad_vendida = (df_selection['Cantidad'].sum()) 
            st.subheader(f"Products sold: {cantidad_vendida:,.2f}")  
        with col2:
            valor_vendida = (df_selection['Valor'].sum()) 
            st.subheader(f"Total Sold: ${valor_vendida:,.2f}")  
        with col3:
            promedio_vendida = (valor_vendida / cantidad_vendida) 
            st.subheader(f"Average Sold: ${promedio_vendida:,.2f}")  


        col4, col5 = st.columns(2)
        with col4:
            bar_chart = px.bar(df_selection,
                               x = 'Hora',
                               y = 'Cantidad',
                               color = 'Producto',
                               )

            bar_chart.update_layout(
                font=dict(
                family="Courier New, monospace",
                size=15,
                color="white"
            )
            )

            bar_chart.for_each_xaxis(lambda x: x.update(showgrid=False))  # This will delete the grid for both x and y axis   
            st.plotly_chart(bar_chart)

        with col5:
            all_products_sold = df_selection.groupby(by=["Producto"]).sum()[["Cantidad"]]
 
            products_sold = px.pie(
            all_products_sold,
            values = 'Cantidad',
            names = all_products_sold.index
            )
            products_sold.update_layout(height = 500, showlegend= False)
            products_sold.update_traces(textposition = 'inside', textinfo = 'percent+label', hole = .3)            
            st.plotly_chart(products_sold) 

    if select_product == 'Wines':
        @st.cache_data
        def get_data_from_excel():    
                excel_file = 'POSTO SALES.xlsx'
                sheet_name = 'WINES'
                df = pd.read_excel(excel_file,
                          sheet_name = sheet_name,
                          usecols = 'A:D',
                          nrows = 281)
                return df
        df = get_data_from_excel()
# 

        producto = st.sidebar.multiselect("Select the Product:",
                                   options= df["Producto"].unique(),
                                   default= df["Producto"].unique()
                                   )
        Hora = st.sidebar.multiselect("Select the Hour:",
                                   options= df["Hora"].unique(),
                                   default= df["Hora"].unique()
                                   )
        df_selection = df.query(
                                "Producto == @producto & Hora == @Hora" 

        )
        col1, col2, col3 = st.columns(3)
        with col1:
            cantidad_vendida = (df_selection['Cantidad'].sum()) 
            st.subheader(f"Amount of Products: {cantidad_vendida:,.2f}")  
        with col2:
            valor_vendida = (df_selection['Valor'].sum()) 
            st.subheader(f"Total Sold: ${valor_vendida:,.2f}") 
        with col3:
            promedio_vendida = (valor_vendida / cantidad_vendida) 
            st.subheader(f"Average Sold: ${promedio_vendida:,.2f}")  


        col4, col5 = st.columns(2)
        with col4:
            bar_chart = px.bar(df_selection,
                               x = 'Hora',
                               y = 'Cantidad',
                               color = 'Producto',
                               )

            bar_chart.update_layout(
                font=dict(
                family="Courier New, monospace",
                size=15,
                color="white"
            )
            )

            bar_chart.for_each_xaxis(lambda x: x.update(showgrid=False))  # This will delete the grid for both x and y axis   
            st.plotly_chart(bar_chart)

        with col5:
            all_products_sold = df_selection.groupby(by=["Producto"]).sum()[["Cantidad"]]
 
            products_sold = px.pie(
            all_products_sold,
            values = 'Cantidad',
            names = all_products_sold.index
            )
            products_sold.update_layout(height = 500, showlegend= False)
            products_sold.update_traces(textposition = 'inside', textinfo = 'percent+label', hole = .3)            
            st.plotly_chart(products_sold) 
                      
    if select_product == 'Sweets & Others':
        @st.cache_data
        def get_data_from_excel():    
                excel_file = 'POSTO SALES.xlsx'
                sheet_name = 'SWEETS'
                df = pd.read_excel(excel_file,
                          sheet_name = sheet_name,
                          usecols = 'A:D',
                          nrows = 125)
                return df
        df = get_data_from_excel()
# 

        producto = st.sidebar.multiselect("Select the Product:",
                                   options= df["Producto"].unique(),
                                   default= df["Producto"].unique()
                                   )
        Hora = st.sidebar.multiselect("Select the Hour:",
                                   options= df["Hora"].unique(),
                                   default= df["Hora"].unique()
                                   )
        df_selection = df.query(
                                "Producto == @producto & Hora == @Hora" 

        )
        col1, col2, col3 = st.columns(3)
        with col1:
            cantidad_vendida = (df_selection['Cantidad'].sum()) 
            st.subheader(f"Amount of Products: {cantidad_vendida:,.2f}")  
        with col2:
            valor_vendida = (df_selection['Valor'].sum()) 
            st.subheader(f"Total Sold: ${valor_vendida:,.2f}") 
        with col3:
            promedio_vendida = (valor_vendida / cantidad_vendida) 
            st.subheader(f"Average Sold: ${promedio_vendida:,.2f}")  


        col4, col5 = st.columns(2)
        with col4:
            bar_chart = px.bar(df_selection,
                               x = 'Hora',
                               y = 'Cantidad',
                               color = 'Producto',
                               )

            bar_chart.update_layout(
                font=dict(
                family="Courier New, monospace",
                size=15,
                color="white"
            )
            )

            bar_chart.for_each_xaxis(lambda x: x.update(showgrid=False))  # This will delete the grid for both x and y axis   
            st.plotly_chart(bar_chart)

        with col5:
            all_products_sold = df_selection.groupby(by=["Producto"]).sum()[["Cantidad"]]
 
            products_sold = px.pie(
            all_products_sold,
            values = 'Cantidad',
            names = all_products_sold.index
            )
            products_sold.update_layout(height = 500, showlegend= False)
            products_sold.update_traces(textposition = 'inside', textinfo = 'percent+label', hole = .3)            
            st.plotly_chart(products_sold) 
          
                        
    if select_product == 'Beers':
        @st.cache_data
        def get_data_from_excel():    
                excel_file = 'POSTO SALES.xlsx'
                sheet_name = 'BEERS'
                df = pd.read_excel(excel_file,
                          sheet_name = sheet_name,
                          usecols = 'A:D',
                          nrows = 144)
                return df
        df = get_data_from_excel()
# 

        producto = st.sidebar.multiselect("Select the Product:",
                                   options= df["Producto"].unique(),
                                   default= df["Producto"].unique()
                                   )
        Hora = st.sidebar.multiselect("Select the Hour:",
                                   options= df["Hora"].unique(),
                                   default= df["Hora"].unique()
                                   )
        df_selection = df.query(
                                "Producto == @producto & Hora == @Hora" 

        )
        col1, col2, col3 = st.columns(3)
        with col1:
            cantidad_vendida = (df_selection['Cantidad'].sum()) 
            st.subheader(f"Amount of Products: {cantidad_vendida:,.2f}")  
        with col2:
            valor_vendida = (df_selection['Valor'].sum()) 
            st.subheader(f"Total Sold: ${valor_vendida:,.2f}") 
        with col3:
            promedio_vendida = (valor_vendida / cantidad_vendida) 
            st.subheader(f"Average Sold: ${promedio_vendida:,.2f}")  


        col4, col5 = st.columns(2)
        with col4:
            bar_chart = px.bar(df_selection,
                               x = 'Hora',
                               y = 'Cantidad',
                               color = 'Producto',
                               )

            bar_chart.update_layout(
                font=dict(
                family="Courier New, monospace",
                size=15,
                color="white"
            )
            )

            bar_chart.for_each_xaxis(lambda x: x.update(showgrid=False))  # This will delete the grid for both x and y axis   
            st.plotly_chart(bar_chart)

        with col5:
            all_products_sold = df_selection.groupby(by=["Producto"]).sum()[["Cantidad"]]
 
            products_sold = px.pie(
            all_products_sold,
            values = 'Cantidad',
            names = all_products_sold.index
            )
            products_sold.update_layout(height = 500, showlegend= False)
            products_sold.update_traces(textposition = 'inside', textinfo = 'percent+label', hole = .3)            
            st.plotly_chart(products_sold) 