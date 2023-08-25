import pandas as pd
import streamlit as st
import plotly.graph_objects as go


# Function to load data
def load_data(file_name: str):
    return pd.read_csv(file_name, encoding='utf-8')

# Function to plot data
def plot_data(data, score, score_interval, std, title, threshold_score):
    scatter = go.Scatter(
        x=data['team'],
        y=data[score],
        mode='markers',
        marker_symbol='diamond',
        marker=dict(
            size = 12,
            color='#580BE6'),
        error_y=dict(
            type='data',
            array=data[std],
            visible=True
        ))

    layout = go.Layout(
        yaxis_title="Score",
        xaxis_title="Teams",
        xaxis = dict(showgrid=True, tickangle = -90),
        yaxis = dict(showgrid=True),
        yaxis_range=score_interval
    )

    fig = go.Figure(data = [scatter], layout=layout)
    fig.add_hline(y=threshold_score, line_dash="dot",
                  annotation_text="threshold score: {}".format(threshold_score),
                  annotation_position="bottom right",
                  annotation_font_size=20,
                  line_color="plum",
                  annotation_font_color="plum"
                  )
    st.plotly_chart(fig, use_container_width=True)


# General Setup
st.title('Baubap AI Challenge - Dashboard')

# Load data

# Neural Network Model
st.header("Neural Network Model")
plot_data(load_data('./data/data_challenge01.csv'),
          "score", [0,1], "std",
          "Neural Network Model", 0.25)

# Time Series Model
st.header("Time Series Model")
plot_data(load_data('./data/data_challenge02.csv'),
          "score", [0.5e6,7.0e6], "std",
          "Time Series Model", 1.5e6)
