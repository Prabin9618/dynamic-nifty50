import streamlit as st
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('final_nifty_dec23.csv')

fig = go.Figure([go.Scatter(x=df.ds,y=df.yhat)])
fig.update_xaxes(title_text='Date')
fig.update_yaxes(title_text='Closing')
fig.update_layout(title="NIFTY Index upto next 5 months")

st.plotly_chart(fig, use_container_width=False)