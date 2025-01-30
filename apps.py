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
try:
    data = pd.read_csv(url)
except Exception as e:
    st.error(f"Failed to load dataset from {url}. Error: {e}")
    st.stop()

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
        # Helper function to load JSON
        def load_json_from_github(url):
            try:
                response = requests.get(url)
                response.raise_for_status()
                return pio.from_json(response.text)
            except requests.exceptions.RequestException as req_err:
                st.error(f"HTTP error occurred while fetching {url}: {req_err}")
            except ValueError as json_err:
                st.error(f"JSON decoding error for {url}: {json_err}")
            except Exception as e:
                st.error(f"An unexpected error occurred: {e}")
            return None

        # List of figures to load
        figures = [
            {"title": "Total price by product category", "url": "https://raw.githubusercontent.com/Abdallah00Mohamed00Elsayed/project_analysis/master/fig1.json"},
            {"title": "Relation between product weight and price", "url": "https://raw.githubusercontent.com/Abdallah00Mohamed00Elsayed/project_analysis/master/fig2.json"},
            {"title": "The highest month that has orders", "url": "https://raw.githubusercontent.com/Abdallah00Mohamed00Elsayed/project_analysis/master/fig3.json"},
            {"title": "The highest day that has orders", "url": "https://raw.githubusercontent.com/Abdallah00Mohamed00Elsayed/project_analysis/master/fig4.json"},
            {"title": "The highest season that has orders", "url": "https://raw.githubusercontent.com/Abdallah00Mohamed00Elsayed/project_analysis/master/Q5.csv", "type": "csv", "plot_func": "bar", "x": "order_approved_at_date_Month_Seasont", "y": "order_count", "color": "order_approved_at_date_Month_Seasont", "labels": {"order_approved_at_date_Month_Seasont": "Season Name", "order_count": "Total Order Count"}},
            {"title": "Number of products sold by sellers", "url": "https://raw.githubusercontent.com/Abdallah00Mohamed00Elsayed/project_analysis/master/Q6.csv", "type": "csv", "plot_func": "bar", "x": "seller_id", "y": "product_count", "color": "product_category", "labels": {"seller_id": "Seller ID", "product_count": "Number of Products"}},
            {"title": "Percentage of late or on-time orders", "url": "https://raw.githubusercontent.com/Abdallah00Mohamed00Elsayed/project_analysis/master/fig7.json"},
            {"title": "Average delivery delay by product category", "url": "https://raw.githubusercontent.com/Abdallah00Mohamed00Elsayed/project_analysis/master/fig_delays.json"},
            {"title": "Average freight value by product category", "url": "https://raw.githubusercontent.com/Abdallah00Mohamed00Elsayed/project_analysis/master/fig8.json"},
            {"title": "The highest review score by product category", "url": "https://raw.githubusercontent.com/Abdallah00Mohamed00Elsayed/project_analysis/master/fig9.json"},
            {"title": "The lowest review score by product category", "url": "https://raw.githubusercontent.com/Abdallah00Mohamed00Elsayed/project_analysis/master/fig10.json"},
            {"title": "Average review score by seller", "url": "https://raw.githubusercontent.com/Abdallah00Mohamed00Elsayed/project_analysis/master/fig11.json"},
            {"title": "Number of orders by state", "url": "https://raw.githubusercontent.com/Abdallah00Mohamed00Elsayed/project_analysis/master/fig12.json"},
            {"title": "City and state: Number of orders", "url": "https://raw.githubusercontent.com/Abdallah00Mohamed00Elsayed/project_analysis/master/fig13.json"},
            {"title": "State and product category orders", "url": "https://raw.githubusercontent.com/Abdallah00Mohamed00Elsayed/project_analysis/master/fig14.json"},
            {"title": "Top 5 states by late percentage", "url": "https://raw.githubusercontent.com/Abdallah00Mohamed00Elsayed/project_analysis/master/fig15.json"},
            {"title": "Average review score by customer state", "url": "https://raw.githubusercontent.com/Abdallah00Mohamed00Elsayed/project_analysis/master/fig17.json"},
            {"title": "Monthly payment value by payment type", "url": "https://raw.githubusercontent.com/Abdallah00Mohamed00Elsayed/project_analysis/master/fig18.json"},
            {"title": "Heatmap of all numerical data", "url": "https://raw.githubusercontent.com/Abdallah00Mohamed00Elsayed/project_analysis/master/fig18_1.json"},
            {"title": "Monthly payment value spending", "url": "https://raw.githubusercontent.com/Abdallah00Mohamed00Elsayed/project_analysis/master/fig19.json"},
            {"title": "Monthly order volume", "url": "https://raw.githubusercontent.com/Abdallah00Mohamed00Elsayed/project_analysis/master/fig20.json"}
        ]

        for fig in figures:
            st.subheader(fig["title"])
            if fig.get("type") == "csv":
                try:
                    df = pd.read_csv(fig["url"])
                    if fig["plot_func"] == "bar":
                        plot = px.bar(
                            df,
                            x=fig["x"],
                            y=fig["y"],
                            color=fig["color"],
                            title=fig
::contentReference[oaicite:0]{index=0}
 
