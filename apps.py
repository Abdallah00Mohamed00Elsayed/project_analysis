import pandas as pd
import streamlit as st
import plotly.io as pio
import plotly.express as px

# Set page configuration
st.set_page_config(
    layout="wide",
    page_title="Brazil Market Analysis",
    page_icon="📊"
)
data = pd.read_csv(r"E:\python_session\Sessions\preprocessing\archive (1)\project\dataproject.csv")


# Streamlit content starts here
st.title("Brazil Market Analysis")
st.write("Welcome to the dashboard!")
page = st.sidebar.selectbox("Choose a Page", ["Dataset", "Analysis"])
data = pd.read_csv("dataproject.csv")

num = data.describe()
cat = data.describe(include = 'O')
if page == 'Dataset':
    st.header('DataSet Head')
    st.dataframe(data.head(20))
    st.subheader("Dataset Information")
    st.write(f"Number of Rows: {data.shape[0]}")
    st.write(f"Number of Columns: {data.shape[1]}")


elif page == "Analysis":
    st.title("Analysis")

    
    tab1, tab2 = st.tabs(["Descriptive Statistics", "Visualizations"])

    
    with tab1:
        
    
        st.subheader('Numerical Describtive Statistics')
        st.dataframe(num.T, 1000, 500)
   
        st.subheader('Categorical Describtive Statistics')
        st.dataframe(cat.T, 1000, 500)

    with tab2:
        st.subheader("total price by product category")
        fig1 = pio.read_json("fig1.json")
        
        st.plotly_chart(fig1,use_container_width=True)
        st.subheader("releation between the product weight and the price")
        fig2 = pio.read_json("fig2.json")  
        st.plotly_chart(fig2, use_container_width=True)
        st.subheader("the highest month that have orders")
        fig3 = pio.read_json("fig3.json")  
        st.plotly_chart(fig3, use_container_width=True)
        st.subheader("the highest day that have orders ")
        fig4 = pio.read_json("fig4.json")  
        st.plotly_chart(fig4, use_container_width=True)
        Q5 = pd.read_csv('Q5.csv')
        fig5 = px.bar(Q5,
             x='order_approved_at_date_Month_Seasont',
             y='order_count',
                color='order_approved_at_date_Month_Seasont',
              title='the highest season that have the orders',
              labels={'order_approved_at_date_Month_Seasont':'season name','order_count':'total order count'}
                ,width=900,height=500,
             )
        st.subheader("highest season that have orders ")
        st.plotly_chart(fig5, use_container_width=True)
        st.subheader("number of products sold by sellers ")
        Q6 = pd.read_csv('Q6.csv')
        fig6 = px.bar(Q6,
             x='seller_id',
             y='product_count',
             color='product_category',
             title='Number of Products Sold by Sellers',
              labels={'seller_id': 'Seller ID', 'product_count': 'Number of Products'},width=900,height=500,)
        st.plotly_chart(fig6, use_container_width=True)
        st.subheader("the percentage of late or on_time orders")
        fig7 = pio.read_json("fig7.json")  
        st.plotly_chart(fig7, use_container_width=True)
        st.subheader("average delivery delay by-product category ")
        fig_delays = pio.read_json("fig_delays.json")  
        st.plotly_chart(fig_delays, use_container_width=True)
        st.subheader("average freight value by product  category ")
        fig8 = pio.read_json("fig8.json")  
        st.plotly_chart(fig8, use_container_width=True)
        st.subheader("the highest review score by product_catogery  ")
        fig9 = pio.read_json("fig9.json")  
        st.plotly_chart(fig9, use_container_width=True)
        st.subheader("the lowest review score product_catogery  ")
        fig10 = pio.read_json("fig10.json")  
        st.plotly_chart(fig10, use_container_width=True)
        st.subheader("the relation between review score and delay_days")
        fig10_1 = pio.read_json("fig10_1.json")  
        st.plotly_chart(fig10_1, use_container_width=True)
        st.subheader("AVG rewiew score by seller")
        fig11 = pio.read_json("fig11.json")  
        st.plotly_chart(fig11, use_container_width=True)
        st.subheader("number of orders by state")
        fig12 = pio.read_json("fig12.json")  
        st.plotly_chart(fig12, use_container_width=True)
        st.subheader("ity and state , number of order")
        fig13 = pio.read_json("fig13.json")  
        st.plotly_chart(fig13, use_container_width=True)
        st.subheader("state and product_catogery order")
        fig14 = pio.read_json("fig14.json")  
        st.plotly_chart(fig14, use_container_width=True)
        st.subheader("top 5 states by late percentage ")
        fig15 = pio.read_json("fig15.json")  
        st.plotly_chart(fig15, use_container_width=True)
        st.subheader("avg review score by customer state ")
        fig17 = pio.read_json("fig17.json")  
        st.plotly_chart(fig17, use_container_width=True)
        st.subheader("monthly payment value by payment type")
        fig18 = pio.read_json("fig18.json")  
        st.plotly_chart(fig18, use_container_width=True)
        st.subheader("monthly payment value spending")
        fig19 = pio.read_json("fig19.json")  
        st.plotly_chart(fig19, use_container_width=True)
        st.subheader("monthly order volume")
        fig20 = pio.read_json("fig20.json")  
        st.plotly_chart(fig20, use_container_width=True)
        st.subheader("heatmap of all numreical data")
        fig18_1 = pio.read_json("fig18_1.json")  
        st.plotly_chart(fig18_1, use_container_width=True)
