import streamlit as st
import pandas as pd

st.title('🤖 streamlitapp')

st.info('Ceci est une application streamlit')
df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/penguins-heroku/refs/heads/master/penguins_example.csv)
df
