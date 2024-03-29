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
    @st.cache_data  # This will cache the file(s) 
    def get_data_from_excel():
        df = pd.read_excel(
        io = excel_file, 
        sheet_name='APRIL', 
        usecols='B:AU',
        nrows=33
        )
        return df
    df = get_data_from_excel()

    st.title(":pizza: April Sales")
    st.markdown("##")

    total_cash = (df["EFECTIVO"].sum())   # Creating variables to get the sum from a selected row/column of my dataframe 
    total_cards = (df['Tarjetas'].sum())
    total_sales = (df['TOTAL'].sum())
    average_salesApril = total_sales / df['Cobrados'].sum()
    average_perDay = total_sales / 24

    cash_column, card_column, average_column, average_perDay_column, total_column = st.columns(5)
    with cash_column:                                          # Getting the sum and displaying it in a column
        st.subheader("Total Cash:")
        st.subheader(f"US $ {total_cash:,.2f}")
    with card_column:
        st.subheader("Total Cards:")
        st.subheader(f"US $ {total_cards:,.2f}") 
    with average_column:
        st.subheader("Average Per Sale:") 
        st.subheader(f"US ${average_salesApril:,.2f}")
    with average_perDay_column:
        st.subheader("Average Per Day:")
        st.subheader(f"US ${average_perDay:,.2f}")
    with total_column:
        st.subheader("Total Sales:")
        st.subheader(f"US ${total_sales:,.2f}")  
    st.markdown("---")

    top5_column, sales_by_hour_column = st.columns(2)

    sales_by_product = df.groupby(by=["Product"]).sum()[["Total Sold"]].sort_values(by="Total Sold")
    # A variable that will group my dataframe from the selected columns. Product X Total Sold
    with top5_column:
        products_Sales = px.bar(   # Once grouped it allows me display the dataframe in a bar chart Product(x) X Total Sold(y)
            sales_by_product,
            x="Total Sold",
            y=sales_by_product.index,
            orientation = "h",
            title = "<b>Top 5 Products Sold</b>",
            color_discrete_sequence=["#0083B8"] * len(sales_by_product),
            template = "plotly_white"
        )

        products_Sales.update_layout(
            plot_bgcolor = "rgba(0,0,0,0)",
            xaxis=(dict(showgrid=False))   # xaxis on the chart wll be hidden
        )

        st.plotly_chart(products_Sales)    

    with sales_by_hour_column:
        sales_by_hour = df.groupby(by=["Time"]).sum() # Grouping the "Time" columns and adding its values
                                                      # I am grouping every hour of the day for the whole year and adding the values.
        sold_by_the_hour = px.bar(
            sales_by_hour,
            x=sales_by_hour.index,
            y="Total Per Hour",
            title = "<b>Sales by Hour</b>",
            color_discrete_sequence=["#0083B8"] * len(sales_by_hour),
            template = "plotly_white"
        )
        sold_by_the_hour.update_layout(
            xaxis=dict(tickmode="linear"),
            plot_bgcolor= "rgba(0,0,0,0)",
            yaxis=(dict(showgrid=False))
        )
        st.plotly_chart(sold_by_the_hour)

    soldPerHourColumn, productsPie = st.columns(2)

    with soldPerHourColumn:
        fg_sales = df.groupby(by=["Product"]).sum()[["Hora 11" , "Hora 12" , "Hora 13" ,"Hora 14" , "Hora 15" , "Hora 16" , "Hora 17" ,"Hora 18" , "Hora 19" , "Hora 20" , "Hora 21" , "Hora 22" , "Hora 23"]]
                                # Grouping each product with the hour of the day to gather the data
        sales_hour = px.bar(    # It will return the sum of each hour with the name of the product
                fg_sales,
                x=fg_sales.index,
                y=["Hora 11" , "Hora 12" , "Hora 13", "Hora 14" , "Hora 15" , "Hora 16" , "Hora 17" ,"Hora 18" , "Hora 19" , "Hora 20" , "Hora 21" , "Hora 22" , "Hora 23"],
                title = "<b>Top 5 Products Sold Per Hour</b>",
                template = "plotly_white",
            )
        sales_hour.update_layout(
                plot_bgcolor = "rgba(0,0,0,0)",
                xaxis=(dict(showgrid=False)),
                yaxis=(dict(showgrid=False))    
        )
        st.plotly_chart(sales_hour)

    with productsPie:
        all_products_sold = df.groupby(by=["Producto"]).sum()[["Cantidad"]]  # Creating a pie chart that returns the dataframe of the sum of each product sold

        products_sold = px.pie(
                all_products_sold,
                values = 'Cantidad',
                names = all_products_sold.index,
        )

        products_sold.update_layout(height = 500, showlegend= False, title_text='<b>All Products Sold</b>')
        products_sold.update_traces(textposition = 'inside', textinfo = 'percent+label') # Labeling the pie chart to hide texts, etc.
        st.plotly_chart(products_sold)        

    april_tab = st.sidebar.checkbox('📉Expenses') # Checkbox button widge to display the expenses if wish to see

    inventory_expenses = (df["Cost"].sum()) 
    employee_expenses = (df["Salary"].sum())
    total_expenses = (df["Cost"]).sum() + (df["Salary"]).sum()

    if april_tab:
        st.title(":chart_with_downwards_trend: Expenses")
        st.markdown("##")
        inv_expense_column, employee_salary_column, total_expenses_column = st.columns(3)
        with inv_expense_column:
            st.subheader("Inventory Expenses:")
            st.subheader(f"US $ {inventory_expenses:,.2f}")
        with employee_salary_column:
            st.subheader("Employee Salaries:")
            st.subheader(f"US $ {employee_expenses:,.2f}")
        with total_expenses_column:
            st.subheader("Total Expenses:")
            st.subheader(f"US $ {total_expenses:,.2f}")
        st.markdown("---")
        #
        april_expense_column, april_expense_pie_column = st.columns(2)
        
        with april_expense_column:
            aprilExpenses = df.groupby(by=(["Expenses"])).sum()[["Cost"]].sort_values(by="Cost")

            expenses = px.bar(
                    aprilExpenses,
                    x="Cost",
                    y=aprilExpenses.index,
                    orientation='h',
                    color_discrete_sequence=px.colors.sequential.RdBu,
                    template = "plotly_white"
                )
                
            expenses.update_layout(
                    plot_bgcolor = "rgba(0,0,0,0)",
                    xaxis=(dict(showgrid=False)),
                    yaxis=(dict(showgrid=False))
                )
            st.plotly_chart(expenses)

        with april_expense_pie_column:
            expenses_pie = df.groupby(by=["Item"]).sum()[["Expense"]]

            expenses_pie_ = px.pie(
                    expenses_pie,
                    values = 'Expense',
                    names = expenses_pie.index,
                    hole = .2,
                    color_discrete_sequence=px.colors.sequential.RdBu
            )
            st.plotly_chart(expenses_pie_)  