import pandas as pd
import streamlit as st
import plotly.graph_objects as go


# Function to load data
def load_data(file_name: str):
    return pd.read_csv(file_name, encoding='utf-8')

# Function to plot data
def plot_data(data, score, std, title, goal_score):
    scatter = go.Scatter(
        x=data['team'],
        y=data[score],
        mode='markers',
        marker=dict(
            color='#580BE6'),
        error_y=dict(
            type='data',
            array=data[std],
            visible=True
        ))

    layout = go.Layout(
        yaxis_title="score",
        xaxis_title="Teams",
        yaxis_range=[0,1.2]
    )

    fig = go.Figure(data = [scatter], layout=layout)
    fig.add_hline(y=goal_score, line_dash="dot",
                  annotation_text="goal score",
                  annotation_position="bottom right",
                  annotation_font_size=20,
                  line_color="plum",
                  annotation_font_color="plum"
                  )
    st.plotly_chart(fig, use_container_width=True)


# General Setup
st.title('Baubap AI Challenge - Dashboard')

# Load data
data = load_data('./data/data.csv')

# Neural Network Model
st.subheader("Neural Network Model")
plot_data(data, "score", "std", "Neural Network Model", 0.25)

# Time Series Model
st.subheader("Time Series Model")
plot_data(data, "score", "std", "Time Serie Model", 0.99)
