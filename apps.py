import os
import pandas as pd
import streamlit as st
import plotly.io as pio
import plotly.express as px
import requests

# Set page configuration
st.set_page_config(
    layout="wide",
    page_title="Brazil Market Analysis",
    page_icon="📊"
)

# Load dataset from GitHub
url = "https://raw.githubusercontent.com/Abdallah00Mohamed00Elsayed/project_analysis/master/dataproject.csv"
data = pd.read_csv(url)

# Streamlit content starts here
st.title("Brazil Market Analysis")
st.write("Welcome to the dashboard!")
page = st.sidebar.selectbox("Choose a Page", ["Dataset", "Analysis"])

num = data.describe()
cat = data.describe(include='O')

if page == 'Dataset':
    st.header('Dataset Head')
    st.dataframe(data.head(20))
    st.subheader("Dataset Information")
    st.write(f"Number of Rows: {data.shape[0]}")
    st.write(f"Number of Columns: {data.shape[1]}")

elif page == "Analysis":
    st.title("Analysis")
    tab1, tab2 = st.tabs(["Descriptive Statistics", "Visualizations"])

    with tab1:
        st.subheader('Numerical Descriptive Statistics')
        st.dataframe(num.T, 1000, 500)

        st.subheader('Categorical Descriptive Statistics')
        st.dataframe(cat.T, 1000, 500)

    with tab2:
        # Helper function to load JSON with error handling
        def load_json_from_github(url):
            response = requests.get(url, headers={"Cache-Control": "no-cache"})
            if response.status_code == 200:
                try:
                    return pio.from_json(response.text)
                except Exception as e:
                    st.error(f"JSON Parse Error: {e}\nError in file: {url}")
                    return None
            else:
                st.error(f"Error loading {url}. HTTP Status: {response.status_code}")
                return None

        # List of visualizations
        json_files = [
            ("Total price by product category", "fig1.json"),
            ("Relation between product weight and price", "fig2.json"),
            ("The highest month that has orders", "fig3.json"),
            ("The highest day that has orders", "fig4.json"),
            ("The highest review score by product category", "fig9.json"),
            ("The lowest review score by product category", "fig10.json"),
            ("Average review score by seller", "fig11.json"),
            ("Number of orders by state", "fig12.json"),
            ("City and state: Number of orders", "fig13.json"),
            ("State and product category orders", "fig14.json"),
            ("Top 5 states by late percentage", "fig15.json"),
            ("Average review score by customer state", "fig17.json"),
            ("Monthly payment value by payment type", "fig18.json"),
            ("Heatmap of all numerical data", "fig18_1.json"),
            ("Monthly payment value spending", "fig19.json"),
            ("Monthly order volume", "fig20.json"),
        ]

        base_url = "https://raw.githubusercontent.com/Abdallah00Mohamed00Elsayed/project_analysis/master/"

        for title, filename in json_files:
            st.subheader(title)
            fig = load_json_from_github(base_url + filename)
            if fig:
                st.plotly_chart(fig, use_container_width=True)

        # Special cases with CSVs
        st.subheader("The highest season that has orders")
        Q5_url = base_url + "Q5.csv"
        try:
            Q5 = pd.read_csv(Q5_url)
            fig5 = px.bar(
                Q5,
                x='order_approved_at_date_Month_Seasont',
                y='order_count',
                color='order_approved_at_date_Month_Seasont',
                title='The highest season that has orders',
                labels={'order_approved_at_date_Month_Seasont': 'Season Name', 'order_count': 'Total Order Count'},
                width=900,
                height=500,
            )
            st.plotly_chart(fig5, use_container_width=True)
        except Exception as e:
            st.error(f"Error loading CSV: {Q5_url}\n{e}")

        st.subheader("Number of products sold by sellers")
        Q6_url = base_url + "Q6.csv"
        try:
            Q6 = pd.read_csv(Q6_url)
            fig6 = px.bar(
                Q6,
                x='seller_id',
                y='product_count',
                color='product_category',
                title='Number of Products Sold by Sellers',
                labels={'seller_id': 'Seller ID', 'product_count': 'Number of Products'},
                width=900,
                height=500,
            )
            st.plotly_chart(fig6, use_container_width=True)
        except Exception as e:
            st.error(f"Error loading CSV: {Q6_url}\n{e}")
