import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')
df = pd.read_csv('census_india.csv')

list_of_states = list(df['State'].unique())
list_of_states.insert(0,'Entire India')

st.sidebar.title('Data Visualization of Census (India)')

selected_state = st.sidebar.selectbox('Select State', list_of_states)
primary = st.sidebar.selectbox('Select Primary Parameter', sorted(df.columns[5:]))
secondary = st.sidebar.selectbox('Select Secondary Parameter', sorted(df.columns[5:]))

plot_button = st.sidebar.button('Plot Graph')
if plot_button:
    st.text('Bubble size represents primary parameter')
    st.text('Bubble color represents secondary parameter')
    if selected_state == 'Entire India':
        fig = px.scatter_map(df, lat='Latitude', lon='Longitude', size=primary, color=secondary, zoom=4, size_max=35,
                                width=1200, height=700, hover_name='District')
    else:
        state_df = df[df['State']==selected_state]
        fig = px.scatter_map(state_df, lat='Latitude', lon='Longitude', size=primary, color=secondary, zoom=5, size_max=35,
                                width=1200, height=700, hover_name='District')
    st.plotly_chart(fig)
