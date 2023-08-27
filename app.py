import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go


# Function to load data
def load_data(file_name: str):
    return pd.read_csv(file_name, encoding='utf-8')

# Format function for a better display on Time Series Model threshold
def format_score(score):
    if score >= 1e6:
        return '{:.2f}M'.format(score / 1e6)
    else:
        return '{:.2f}'.format(score)

# Function to plot data
def plot_data(data, score, score_interval, std, title, threshold_score):
    colors = ['blue', 'green', 'red', 'purple', 'orange', 'pink', 'brown', 'cyan', 'magenta', 'lime', 'yellow', 'teal']

    light_purple = 'rgb(180, 140, 220)'

    scatter = go.Scatter(
        x=data['team'],
        y=data[score],
        mode='markers',
        marker_symbol='diamond',
        marker=dict(
            size = 12,
            color=colors[:len(data)]),
        error_y=dict(
            type='data',
            array=data[std],
            visible=True,
            color = 'white'
        ))

    layout = go.Layout(
        yaxis_title="Score",
        xaxis_title="Teams",
        xaxis = dict(showgrid=True, tickangle = -90),
        yaxis = dict(showgrid=True),
        yaxis_range=score_interval
    )

    formatted_threshold_score = format_score(threshold_score)

    fig = go.Figure(data = [scatter], layout=layout)
    fig.add_hline(y=threshold_score, line_dash="dot",
                  annotation_text="Threshold Score: {}".format(formatted_threshold_score),
                  annotation_position="bottom right",
                  annotation_font_size=20,
                  line_color=light_purple,
                  annotation_font_color=light_purple
                  )
    st.plotly_chart(fig, use_container_width=True)



# General Setup
st.title('Baubap AI Challenge - Dashboard')

# Load data

# Neural Network Model
st.header("Neural Network Model")
plot_data(load_data('./data/data_challenge01.csv'),
          "score", [0,1.2], "std",
          "Neural Network Model", 0.25)

# Time Series Model
st.header("Time Series Model")
plot_data(load_data('./data/data_challenge02.csv'),
          "score", [0.25e6,12.0e6], "std",
          "Time Series Model", 2.5e6)
