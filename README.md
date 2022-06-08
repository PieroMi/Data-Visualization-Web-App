<h1 align="center">Interactive Financial Dashboard</h1>

<h2 align="center">

<img src="Posto Letrero.png" width="100%">

_An interactive financial dashboard for my pizza parlor business_

<a  href="https://share.streamlit.io/pieromi/data-visualization-web-app/main/app.py">➡️Live Demo⬅️</a>


</h2>

<h2 align="center">

<img src="https://media.giphy.com/media/bIPNNUW0ghs0PjdvlZ/giphy.gif" width="50%">

<img src="https://media.giphy.com/media/Uf0Vhq219YuwgAqc6b/giphy.gif" width="50%">


</h2>

# Description

Gathered financial data from the pizza parlor to be able to make an interactive financial dashboard. This has allowed me to have a better track of the finances by using different set of tools such as KPIs and APIs to meet certain financial objectives and what to avoid for the future. I was able to use technologies such as the framework <a  href="https://streamlit.io/">Streamlit</a> and gather the data to make a web app. The programming language is purely in <a  href="https://www.python.org/">Python</a>. In addition, I used libraries such as <a  href="https://plotly.com/">Plotly</a> and <a  href="https://pandas.pydata.org/">Pandas</a> that allowed me to use graphing libraries to have in depth analysis of my data. 


# 📝About the project

### 📌Object Oriented Framework

At the time when I made the application there wasn't an option to create multiple pages for one web app. The way I solved this problem was to create an **object oriented application** instead. Created a class called 'Multipage' and within the page it contained the **constuctor** and the **method** classes to click from various different months from the financial report.

<img src="screenies\sidebarmonthly.png" width="20%">

```python {
# To manage multiple apps in the program
class Multipage:

    def __init__(self) -> None:
        # Constructor class to generate a list which will store all the monthly applications as an instance variable
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

```
### 📌Streamlit widget functions

Used widget functions that allowed me to switch from one page to another. These APIs can help me switch from a report of year X to year Y. This tool facilitated the organization of my code because I could partition the monthly reports, the yearly report summaries, and also analysis of the products, instead of coding everything in one page. 

<img src="screenies\sidebarpic.png" width="20%">

```python {
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

```
### 📌Machine Learning & Data Visualization

With the help of the APIs offered by Streamlit I was able to automate certain results based on the input of the user. When I want to do in-depth analysis of the products I either evaluate ALL the products with all the work hours selected or I can select certain product(s) along with the hour(s) selected. Based on what is selected my application is able to return the total of products sold, how much is sold, and the average per product sold. This automation allows me to mutate, visualize and share the data with my colleagues to improve the overall performance of the business.


 _Changing products_

<img src="https://media.giphy.com/media/xNR0xiZjMyQYDkYkx5/giphy.gif" width="50%">

_Changing the hours_

<img src="https://media.giphy.com/media/WGzKVpORRAwumH3Tsd/giphy.gif" width="50%">


```python {
    product = ['', 'Slices', 'Pizzas', 'Drinks', 'Wines', 'Beers', 'Sweets & Others']
    select_product = st.sidebar.selectbox("Select A Category To Analyze its Performance", product)

    if select_product == 'Slices':


        producto = st.sidebar.multiselect("Select the Product:",  # The list of products will be displayed in the multiselect widge
                                   options= df["Producto"].unique(),
                                   default= df["Producto"].unique()
                                   )
        Hora = st.sidebar.multiselect("Select the Hour:",
                                   options= df["Hora"].unique(), # Same with the hours
                                   default= df["Hora"].unique()
                                   )

        df_selection = df.query(    # Creating a variable for Product and Hour, so if the value of product changes it queries the hours and its value and vice versa
                                "Producto == @producto & Hora == @Hora"
        )
        col1, col2, col3 = st.columns(3)
        with col1:
            cantidad_vendida = (df_selection['Cantidad'].sum())  # Based on the quantity of products the value of the product and the value in the hour(s) selected will change
            st.subheader(f"Products sold: {cantidad_vendida:,.2f}")  
        with col2:
            valor_vendida = (df_selection['Valor'].sum()) 
            st.subheader(f"Total Sold: ${valor_vendida:,.2f}")  
        with col3:
            promedio_vendida = (valor_vendida / cantidad_vendida) 
            st.subheader(f"Average Sold: ${promedio_vendida:,.2f}")  
```

### Other Functions
_Analyze the products per hour sold_

<img src="https://media.giphy.com/media/JTPYRx13sQn0GCaNiO/giphy.gif" width="50%">

_Click the radio widget button to see expenses_

<img src="https://media.giphy.com/media/glsEJTbed1UPfMh2Ht/giphy.gif" width="50%">
