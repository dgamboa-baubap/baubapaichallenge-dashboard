import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go


st.set_page_config(page_title= 'Baubap AI Challenge - Scores')

# Function to load data
def load_data(file_name: str):
    return pd.read_csv(file_name, encoding='utf-8')

data = load_data('./data/data.csv')

scatter = go.Scatter(
    x=data['team'],
    y=data['score'],
    mode='markers',
    error_y=dict(
        type='data',
        array=data['std'],
        visible=True
    ))

layout = go.Layout(
    title="Score Table",
    yaxis_title="Score",
    xaxis_title="Teams",
    yaxis_range=[0,1.2]
)

fig = go.Figure(data = [scatter], layout=layout)

st.plotly_chart(fig, use_container_width=True)