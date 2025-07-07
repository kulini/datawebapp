import streamlit as st
import pandas as pd
import plotly.express as px
vehicles = pd.read_csv('./vehicles_us.csv')
st.header("This is my header")

#Plotly Express Histogram
fig = px.histogram(vehicles, x='condition')
fig.update_layout(title='Count of Cars by Condition', xaxis_title='Condition', yaxis_title='Count')
st.plotly_chart(fig)

#Plotly Express scatterplot 
fig_scatter = px.scatter(vehicles, x='model_year', y='price')
fig_scatter.update_layout(title='Model Year vs Price', xaxis_title='Model Year', yaxis_title='Price')


#Checkbox 
show_trend = st.checkbox("Show Price Trend")
if show_trend:
    fig_scatter.update_layout(title='Price Trend Over Time')
st.plotly_chart(fig_scatter)

