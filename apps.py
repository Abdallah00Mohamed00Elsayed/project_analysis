%%writefile apps.py
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
        # Helper function to load JSON
        def load_json_from_github(url):
            response = requests.get(url)
            if response.status_code == 200:
                return pio.from_json(response.text)
            else:
                st.error(f"Error loading {url}. HTTP Status: {response.status_code}")
                return None

        # Visualizations (explicitly written for each figure)
        st.subheader("Total price by product category")
        fig1_url = "https://raw.githubusercontent.com/Abdallah00Mohamed00Elsayed/project_analysis/master/fig1.json"
        fig1 = load_json_from_github(fig1_url)
        if fig1:
            st.plotly_chart(fig1, use_container_width=True)

        st.subheader("Relation between product weight and price")
        fig2_url = "https://raw.githubusercontent.com/Abdallah00Mohamed00Elsayed/project_analysis/master/fig2.json"
        fig2 = load_json_from_github(fig2_url)
        if fig2:
            st.plotly_chart(fig2, use_container_width=True)

        st.subheader("The highest month that has orders")
        fig3_url = "https://raw.githubusercontent.com/Abdallah00Mohamed00Elsayed/project_analysis/master/fig3.json"
        fig3 = load_json_from_github(fig3_url)
        if fig3:
            st.plotly_chart(fig3, use_container_width=True)

        st.subheader("The highest day that has orders")
        fig4_url = "https://raw.githubusercontent.com/Abdallah00Mohamed00Elsayed/project_analysis/master/fig4.json"
        fig4 = load_json_from_github(fig4_url)
        if fig4:
            st.plotly_chart(fig4, use_container_width=True)

        st.subheader("The highest season that has orders")
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
        st.plotly_chart(fig5, use_container_width=True)

        st.subheader("Number of products sold by sellers")
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
        st.plotly_chart(fig6, use_container_width=True)

        st.subheader("Percentage of late or on-time orders")
        fig7_url = "https://raw.githubusercontent.com/Abdallah00Mohamed00Elsayed/project_analysis/master/fig7.json"
        fig7 = load_json_from_github(fig7_url)
        if fig7:
            st.plotly_chart(fig7, use_container_width=True)

        st.subheader("Average delivery delay by product category")
        fig_delays_url = "https://raw.githubusercontent.com/Abdallah00Mohamed00Elsayed/project_analysis/master/fig_delays.json"
        fig_delays = load_json_from_github(fig_delays_url)
        if fig_delays:
            st.plotly_chart(fig_delays, use_container_width=True)

        st.subheader("Average freight value by product category")
        fig8_url = "https://raw.githubusercontent.com/Abdallah00Mohamed00Elsayed/project_analysis/master/fig8.json"
        fig8 = load_json_from_github(fig8_url)
        if fig8:
            st.plotly_chart(fig8, use_container_width=True)

        
        st.subheader("The highest review score by product category")
        fig9_url = "https://raw.githubusercontent.com/Abdallah00Mohamed00Elsayed/project_analysis/master/fig9.json"
        fig9 = load_json_from_github(fig9_url)
        if fig9:
            st.plotly_chart(fig9, use_container_width=True)

        st.subheader("The lowest review score by product category")
        fig10_url = "https://raw.githubusercontent.com/Abdallah00Mohamed00Elsayed/project_analysis/master/fig10.json"
        fig10 = load_json_from_github(fig10_url)
        if fig10:
            st.plotly_chart(fig10, use_container_width=True)

                # Figure 11
        st.subheader("Average review score by seller")
        fig11_url = "https://raw.githubusercontent.com/Abdallah00Mohamed00Elsayed/project_analysis/master/fig11.json"
        fig11 = load_json_from_github(fig11_url)
        if fig11:
            st.plotly_chart(fig11, use_container_width=True)

        # Figure 12
        st.subheader("Number of orders by state")
        fig12_url = "https://raw.githubusercontent.com/Abdallah00Mohamed00Elsayed/project_analysis/master/fig12.json"
        fig12 = load_json_from_github(fig12_url)
        if fig12:
            st.plotly_chart(fig12, use_container_width=True)

        # Figure 13
        st.subheader("City and state: Number of orders")
        fig13_url = "https://raw.githubusercontent.com/Abdallah00Mohamed00Elsayed/project_analysis/master/fig13.json"
        fig13 = load_json_from_github(fig13_url)
        if fig13:
            st.plotly_chart(fig13, use_container_width=True)

        # Figure 14
        st.subheader("State and product category orders")
        fig14_url = "https://raw.githubusercontent.com/Abdallah00Mohamed00Elsayed/project_analysis/master/fig14.json"
        fig14 = load_json_from_github(fig14_url)
        if fig14:
            st.plotly_chart(fig14, use_container_width=True)

        # Figure 15
        st.subheader("Top 5 states by late percentage")
        fig15_url = "https://raw.githubusercontent.com/Abdallah00Mohamed00Elsayed/project_analysis/master/fig15.json"
        fig15 = load_json_from_github(fig15_url)
        if fig15:
            st.plotly_chart(fig15, use_container_width=True)

        # Figure 16 (Optional: Add if available)
        # If there is no figure 16, you can skip this step.

        # Figure 17
        st.subheader("Average review score by customer state")
        fig17_url = "https://raw.githubusercontent.com/Abdallah00Mohamed00Elsayed/project_analysis/master/fig17.json"
        fig17 = load_json_from_github(fig17_url)
        if fig17:
            st.plotly_chart(fig17, use_container_width=True)

        # Figure 18
        st.subheader("Monthly payment value by payment type")
        fig18_url = "https://raw.githubusercontent.com/Abdallah00Mohamed00Elsayed/project_analysis/master/fig18.json"
        fig18 = load_json_from_github(fig18_url)
        if fig18:
            st.plotly_chart(fig18, use_container_width=True)

        # Figure 18_1
        st.subheader("Heatmap of all numerical data")
        fig18_1_url = "https://raw.githubusercontent.com/Abdallah00Mohamed00Elsayed/project_analysis/master/fig18_1.json"
        fig18_1 = load_json_from_github(fig18_1_url)
        if fig18_1:
            st.plotly_chart(fig18_1, use_container_width=True)

        # Figure 19
        st.subheader("Monthly payment value spending")
        fig19_url = "https://raw.githubusercontent.com/Abdallah00Mohamed00Elsayed/project_analysis/master/fig19.json"
        fig19 = load_json_from_github(fig19_url)
        if fig19:
            st.plotly_chart(fig19, use_container_width=True)

        # Figure 20
        st.subheader("Monthly order volume")
        fig20_url = "https://raw.githubusercontent.com/Abdallah00Mohamed00Elsayed/project_analysis/master/fig20.json"
        fig20 = load_json_from_github(fig20_url)
        if fig20:
            st.plotly_chart(fig20, use_container_width=True)

