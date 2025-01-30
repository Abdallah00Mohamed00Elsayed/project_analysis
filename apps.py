import os
import pandas as pd
import streamlit as st
import plotly.io as pio
import plotly.express as px
import requests

# Set page configuration
st.set_page_config(layout="wide", page_title="Brazil Market Analysis", page_icon="📊")

# Load dataset from GitHub
url = "https://raw.githubusercontent.com/Abdallah00Mohamed00Elsayed/project_analysis/master/dataproject.csv"
data = pd.read_csv(url)

# Streamlit content
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
        @st.cache_data(ttl=600)  # Cache JSON for 10 minutes
        def load_json_from_github(url):
            response = requests.get(url)
            if response.status_code == 200:
                json_text = response.text.strip()
                if not json_text:
                    st.error(f"Error: JSON file at {url} is empty.")
                    return None

                try:
                    print("Loaded JSON (First 500 chars):", json_text[:500])  # Debugging
                    return pio.from_json(json_text)
                except Exception as e:
                    st.error(f"Error parsing JSON from {url}: {e}")
                    return None
            else:
                st.error(f"Error loading {url}. HTTP Status: {response.status_code}")
                return None

        # JSON figures
        json_figures = {
            "Total price by product category": "fig1.json",
            "Relation between product weight and price": "fig2.json",
            "The highest month that has orders": "fig3.json",
            "The highest day that has orders": "fig4.json",
            "Percentage of late or on-time orders": "fig7.json",
            "Average delivery delay by product category": "fig_delays.json",
            "Average freight value by product category": "fig8.json",
            "The highest review score by product category": "fig9.json",
            "The lowest review score by product category": "fig10.json",
            "Average review score by seller": "fig11.json",
            "Number of orders by state": "fig12.json",
            "City and state: Number of orders": "fig13.json",
            "State and product category orders": "fig14.json",
            "Top 5 states by late percentage": "fig15.json",
            "Average review score by customer state": "fig17.json",
            "Monthly payment value by payment type": "fig18.json",
            "Heatmap of all numerical data": "fig18_1.json",
            "Monthly payment value spending": "fig19.json",
            "Monthly order volume": "fig20.json"
        }

        for title, filename in json_figures.items():
            st.subheader(title)
            fig_url = f"https://raw.githubusercontent.com/Abdallah00Mohamed00Elsayed/project_analysis/master/{filename}"
            fig = load_json_from_github(fig_url)
            if fig:
                st.plotly_chart(fig, use_container_width=True)

        # CSV-based figures
        csv_figures = {
            "The highest season that has orders": ("Q5.csv", "order_approved_at_date_Month_Seasont", "order_count"),
            "Number of products sold by sellers": ("Q6.csv", "seller_id", "product_count")
        }

        for title, (csv_file, x_column, y_column) in csv_figures.items():
            st.subheader(title)
            csv_url = f"https://raw.githubusercontent.com/Abdallah00Mohamed00Elsayed/project_analysis/master/{csv_file}"
            try:
                df = pd.read_csv(csv_url)
                fig = px.bar(
                    df,
                    x=x_column,
                    y=y_column,
                    color=x_column,
                    title=title,
                    labels={x_column: "Category", y_column: "Count"},
                    width=900,
                    height=500
                )
                st.plotly_chart(fig, use_container_width=True)
            except Exception as e:
                st.error(f"Error loading {csv_file}: {e}")
