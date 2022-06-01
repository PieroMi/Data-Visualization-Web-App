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


excel_file = 'POSTO 2022.xlsx' 

def app():
    @st.experimental_memo
    def get_data_from_excel():
        df = pd.read_excel(
        io = excel_file, 
        sheet_name='MAY22', 
        usecols='A:BM',
        nrows=33
        )
        return df
    df = get_data_from_excel()

    st.title(":pizza: May Sales")
    st.markdown("##")

    total_cash = (df["EFECTIVO"].sum())
    total_cards = (df['Tarjetas'].sum())
    total_sales = (df['TOTAL'].sum())
    average_salesJanuary = total_sales / df['Cobrado'].sum()
    average_perDay = total_sales / 26

    cash_column, card_column, average_column, average_perDay_column, total_column = st.columns(5)
    with cash_column:
        st.subheader("Total Cash:")
        st.subheader(f"US $ {total_cash:,.2f}")
        cashmetric = ((3319.5 / total_cash) * 100)  
        metricresult = f"{100 - cashmetric:,.2f}%" 
        cash_column.metric(label = '', value = '', delta = metricresult)  
        cash_column.metric(label = '', value = '', delta = f"{total_cash - 3319.5:,.2f}") 
    with card_column:
        st.subheader("Total Cards:")
        st.subheader(f"US $ {total_cards:,.2f}")
        cardmetric = ((2259.08 / total_cards) * 100)
        metricresultcard = f"{100 - cardmetric:,.2f}%"
        card_column.metric(label = '', value = '', delta = metricresultcard)
        card_column.metric(label = '', value = '', delta = total_cards - 2259.08 )  
    with average_column:
        st.subheader("Average Per Sale:") 
        st.subheader(f"US ${average_salesJanuary:,.2f}")
        averagemetric = ((17.13/ average_salesJanuary) * 100)
        metricresultaverage = f"{100 - averagemetric:,.2f}%"
        average_column.metric(label = '', value = '', delta = metricresultaverage)
        average_column.metric(label = '', value = '', delta = f"{average_salesJanuary - 17.13:,.2f}")
    with average_perDay_column:
        st.subheader("Average Per Day:")
        st.subheader(f"US ${average_perDay:,.2f}")
        perdaymetric = ((246.46 / average_perDay) * 100)
        metricresultperday = f"{100 - perdaymetric:,.2f}%"
        average_perDay_column.metric(label = '', value = '', delta = metricresultperday)
        average_perDay_column.metric(label = '', value = '', delta = f"{average_perDay - 246.46:,.2f}")
    with total_column:
        st.subheader("Total Sales:")
        st.subheader(f"US ${total_sales:,.2f}") 
        totalmetric = ((5668.58 / total_sales) * 100)
        metricresulttotal = f"{100 - totalmetric:,.2f}%"
        total_column.metric(label = '', value = '', delta = metricresulttotal) 
        total_column.metric(label = '', value = '', delta = f"{total_sales - 5668.58:,.2f}")   
    st.markdown("---")

    top5_column, sales_by_hour_column = st.columns(2)

    sales_by_product = df.groupby(by=["Product"]).sum()[["Total Sold"]].sort_values(by="Total Sold")

    with top5_column:
        products_Sales = px.bar(
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
            xaxis=(dict(showgrid=False))
        )

        st.plotly_chart(products_Sales)

    with sales_by_hour_column:
        sales_by_hour = df.groupby(by=["Time"]).sum()

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
        fg_sales = df.groupby(by=["Product"]).sum()[["Hora 14" , "Hora 15" , "Hora 16" , "Hora 17" ,"Hora 18" , "Hora 19" , "Hora 20" , "Hora 21" , "Hora 22" , "Hora 23"]]

        sales_hour = px.bar(
                fg_sales,
                x=fg_sales.index,
                y=["Hora 14" , "Hora 15" , "Hora 16" , "Hora 17" ,"Hora 18" , "Hora 19" , "Hora 20" , "Hora 21" , "Hora 22" , "Hora 23"],
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
        all_products_sold = df.groupby(by=["Producto"]).sum()[["Cantidad"]]

        products_sold = px.pie(
                all_products_sold,
                values = 'Cantidad',
                names = all_products_sold.index,
        )

        products_sold.update_layout(height = 500, showlegend= False, title_text='<b>All Products Sold</b>')
        products_sold.update_traces(textposition = 'inside', textinfo = 'percent+label')
        st.plotly_chart(products_sold)
    

    january_tab = st.sidebar.checkbox('Expenses')

    inventory_expenses = (df["Cost"].sum())
    employee_expenses = (df["Salary"].sum())
    total_expenses = (df["Cost"]).sum() + (df["Salary"]).sum()

    if january_tab:
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
        
        january_expense_column, january_expense_pie_column = st.columns(2)
        
        with january_expense_column:
            januaryExpenses = df.groupby(by=(["Expenses"])).sum()[["Cost"]].sort_values(by="Cost")

            expenses = px.bar(
                    januaryExpenses,
                    x="Cost",
                    y=januaryExpenses.index,
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

        with january_expense_pie_column:
            expenses_pie = df.groupby(by=["Item"]).sum()[["Expense"]]

            expenses_pie_ = px.pie(
                    expenses_pie,
                    values = 'Expense',
                    names = expenses_pie.index,
                    hole = .2,
                    color_discrete_sequence=px.colors.sequential.RdBu
            )
            st.plotly_chart(expenses_pie_)
    