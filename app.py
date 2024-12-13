import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')

st.header("Exploratory Data Analysis: Vehicle Data")

st.write(df.head())

fig = px.histogram(df, x='price', color='condition', nbins=50, title="Price Distribution by Condition")
st.plotly_chart(fig)

fig = px.histogram(df, x='odometer', color='is_4wd', nbins=50, title="Odometer Distribution by 4WD")
st.plotly_chart(fig)

fig = px.scatter(df, x='odometer', y='price', title='Price vs Odometer') 
st.plotly_chart(fig)

fig = px.scatter(df, x='model_year', y='odometer', title="Odometer vs Model Year")
st.plotly_chart(fig)

is_4wd = st.checkbox("Show only 4WD vehicles")
if is_4wd:
    df = df[df['is_4wd'] == 1]
st.write(df.head())

