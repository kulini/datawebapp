import pandas as pd
import numpy as np
import streamlit as st
import plotly_express as px
import seaborn as sns
import matplotlib.pyplot as plt


st.header('Car Sales Advertisements \n Data viewer')
st.write('Include manufacturers with less than 1000 ads')



df = pd.read_csv('vehicles_us.csv')

#Data Correction
df['date_posted'] = pd.to_datetime(df['date_posted'], format ='%Y-%m-%d')
df.isnull().sum()
df.fillna(0,inplace=True)
df.drop_duplicates(inplace=True)
df['model_year'] = df['model_year'].astype(int)

#Data Enrichment 
df[['brand', 'model_type']] = df['model'].str.extract(r'(\w+)\s+(.+)')

#Rearrange the order for the column
last_two_cols = df.columns[-2:]
new_order = list(last_two_cols) + [col for col in df.columns if col not in last_two_cols]
df = df[new_order]


col_to_move = 'model'
cols = [col for col in df.columns if col != col_to_move]
cols.append(col_to_move)
df = df[cols]


#Data viewing
brand_choice = df['brand'].unique()

selected_menu = st.selectbox('Select a brand',brand_choice)
df_filtered = df[df.brand == selected_menu]
df_filtered



#Bar Plot
st.header('Vehicle types by manufacture')

# Sidebar controls for vehicle types selection
vehicle_types = df['type'].unique()  # Extract the unique vehicle types
selected_types = st.sidebar.multiselect('Select Vehicle Types to Display', vehicle_types, default=vehicle_types)

# Filter the DataFrame based on the selected vehicle types
df_filtered = df[df['type'].isin(selected_types)]  # Filter rows based on 'type' values

# Create the Plotly figure with the selected vehicle types
fig = px.bar(df_filtered, x='brand', y='price', color='type', barmode='stack',
             title="Vehicle Types by Manufacturer", labels={'price': 'Price', 'brand': 'Manufacturer'})

# Customize the layout for better readability
fig.update_layout(
    xaxis_title='Manufacturer',
    yaxis_title='Price',
    legend_title_text='Vehicle Type'
)

# Display the plot
st.plotly_chart(fig, use_container_width=True)





# Plot histogram for condition vs model of the year

st.header('Histogram of condition vs model_year')

condition_choice = df['condition'].unique()
selecte_condition = st.sidebar.multiselect('Select Condition', condition_choice, default=condition_choice)

df = df[df['model_year'] > 0]
fig1 = px.histogram(df, x='model_year', color='condition', barmode='overlay', nbins=50,
                   title='Histogram of Condition vs Model Year')

# Customize the layout for better visualization
fig1.update_layout(
    xaxis_title='Model Year',
    yaxis_title='Count',
    legend_title_text='Condition',
    hovermode='x unified'
)

# Display the Plotly chart in Streamlit
st.plotly_chart(fig1, use_container_width=True)


#Compare price distibution between manufacturers
st.header('Compare price distibution between manufacturers')
manufacturer_1 = st.selectbox("Select manufacturer 1", df['brand'].unique())
manufacturer_2 = st.selectbox("Select manufacturer 2", df['brand'].unique())

# Checkbox to normalize the histogram
normalize = st.checkbox("Normalize histogram")

# Filter the data based on the selected manufacturers
df_filtered1 = df[df['brand'].isin([manufacturer_1, manufacturer_2])]


# Plot histogram for price distibution between manufacturers
fig2 = px.histogram(
    df_filtered1, 
    x='price', 
    color='brand', 
    barmode='overlay',
    histnorm='percent' if normalize else None,  # Normalize if checkbox is checked
    title="Price Distribution by Manufacturer"
)

# Customize layout
fig2.update_layout(
    xaxis_title='Price',
    yaxis_title='Percent' if normalize else 'Count',
    legend_title_text='Manufacturer',
    hovermode='x unified'
)

# Display the plot
st.plotly_chart(fig2, use_container_width=True)
