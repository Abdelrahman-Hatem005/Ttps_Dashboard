import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

tips = pd.read_csv("tips.csv")
st.set_page_config(page_title="Tips Dashboard",
                   page_icon="💰",
                   layout="wide",  # "centered" or "wide"
                   initial_sidebar_state="expanded")



st.title("💰 Tips Dashboard")

##########  side bar

st.sidebar.header("Tips Dashboard")
st.sidebar.image("tips.jpg")

st.sidebar.markdown("""
    ### 📊 Restaurant Tips Dashboard
    This dashboard provides insights into restaurant tips data. Use the filters below to explore the data.

    ---

    ### 🔍 What You Can Do:
    * **Filter Data:** Slice by *Day*, *Time*, and *Smoker Status* to see how these factors affect tips and bills.
    * **Interactive Charts:** Explore relationships between total bills and tips, and see how income is distributed by day and time.
""")

####  filtering!!!!!!!!!
cat_filter = st.sidebar.selectbox("Select Categorical (color)", [None, "sex", "smoker", "day", "time"])
num_filter = st.sidebar.selectbox("Select Numerical (size)",[None,"total_bill","tip"])
col_filter = st.sidebar.selectbox("column filter",[None,"sex", "smoker", "day", "time"])
row_filter = st.sidebar.selectbox("row filter",[None,"sex", "smoker", "day", "time"])


st.sidebar.markdown("made by Eng.[Abdelrahman Hatem](https://www.linkedin.com/in/abdellrahman-hatem-9006b7299/)")

##############  Body
tab1, tab2 = st.tabs(["🔍 Main Relationships", "📊 Distribution Charts"])


a1,a2,a3,a4 = st.columns(4)
a1.metric("Max Total Bill",f"${tips['total_bill'].max():.2f}")
a2.metric("Min Total Bill",f"${tips['total_bill'].min():.2f}")
a3.metric("Max Tip",f"${tips['tip'].max():.2f}")
a4.metric("Min Tip",f"${tips['tip'].min():.2f}")

#draw the scatter plot
custom_colors = {
    # If filtering by sex
    "Male": "#25f079", 
    "Female": "#0a60e2",
    
    # If filtering by smoker status
    "Yes": "#ff6b6b", 
    "No": "#4dadf7",
    
    # If filtering by day
    "Thur": "#ffd166", 
    "Fri": "#ef476f", 
    "Sat": "#06d6a0", 
    "Sun": "#118ab2"
}

with tab1:
    st.subheader("Total Bill vs Tip")
    fig=px.scatter(data_frame=tips, x="total_bill",
                   y="tip", color=cat_filter,
                   size=num_filter,
                   facet_col=col_filter,
                   facet_row=row_filter,
                   color_discrete_map=custom_colors,
                   title="Total Bills vs. Tips",
                   labels={"total_bill": "Total Bill", "tip": "Tip"})
    
st.plotly_chart(fig,use_container_width=True)


##another charts
with tab2:
    tab2.subheader("Diagonistic and Day Breakdowns")
    c1,c2,c3= st.columns(3)
    with c1:
        st.subheader("sex vs total_bill")
        fig1=px.bar(data_frame=tips, x="sex", y="total_bill", color=cat_filter, barmode="group")
        st.plotly_chart(fig1,use_container_width=True)
    with c2:
        st.subheader("smoker or Non-smoker vs tips")
        fig2=px.pie(data_frame=tips, values="tip", names="smoker", color=cat_filter,hole=0.3)
        st.plotly_chart(fig2,use_container_width=True)
    with c3:
        st.subheader("days vs tips")
        fig3=px.pie(data_frame=tips, values="tip", names="day", color=cat_filter,hole=0.3)
        st.plotly_chart(fig3,use_container_width=True)