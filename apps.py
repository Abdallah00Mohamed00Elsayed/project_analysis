
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
        # Visualizations using GitHub files
        def load_json_from_github(url):
            response = requests.get(url)
            if response.status_code == 200:
                return pio.from_json(response.text)
            else:
                st.error(f"Error loading {url}. HTTP Status: {response.status_code}")
                return None

        # Figure 1
        st.subheader("Total price by product category")
        fig1_url = "https://raw.githubusercontent.com/Abdallah00Mohamed00Elsayed/project_analysis/master/fig1.json"
        fig1 = load_json_from_github(fig1_url)
        if fig1:
            st.plotly_chart(fig1, use_container_width=True)

        # Figure 2
        st.subheader("Relation between the product weight and the price")
        fig2_url = "https://raw.githubusercontent.com/Abdallah00Mohamed00Elsayed/project_analysis/master/fig2.json"
        fig2 = load_json_from_github(fig2_url)
        if fig2:
            st.plotly_chart(fig2, use_container_width=True)

        # Figure 3
        st.subheader("The highest month that has orders")
        fig3_url = "https://raw.githubusercontent.com/Abdallah00Mohamed00Elsayed/project_analysis/master/fig3.json"
        fig3 = load_json_from_github(fig3_url)
        if fig3:
            st.plotly_chart(fig3, use_container_width=True)

        # Figure 4
        st.subheader("The highest day that has orders")
        fig4_url = "https://raw.githubusercontent.com/Abdallah00Mohamed00Elsayed/project_analysis/master/fig4.json"
        fig4 = load_json_from_github(fig4_url)
        if fig4:
            st.plotly_chart(fig4, use_container_width=True)

        # Figure 5 with Q5.csv
        Q5_url = "https://raw.githubusercontent.com/Abdallah00Mohamed00Elsayed/project_analysis/master/Q5.csv"
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
        st.subheader("Highest season that has orders")
        st.plotly_chart(fig5, use_container_width=True)

        # Figure 6 with Q6.csv
        Q6_url = "https://raw.githubusercontent.com/Abdallah00Mohamed00Elsayed/project_analysis/master/Q6.csv"
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
        st.subheader("Number of products sold by sellers")
        st.plotly_chart(fig6, use_container_width=True)

        # Load additional figures (fig7 to fig20)
        for i in range(7, 21):
            st.subheader(f"Figure {i}")
            fig_url = f"https://raw.githubusercontent.com/Abdallah00Mohamed00Elsayed/project_analysis/master/fig{i}.json"
            fig = load_json_from_github(fig_url)
            if fig:
                st.plotly_chart(fig, use_container_width=True)
