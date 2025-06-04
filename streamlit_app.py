import streamlit as st
import pandas as pd

st.title('🤖 Machine learning')

st.info('Ceci est une application streamlit')
df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/penguins-heroku/refs/heads/master/penguins_example.csv')
a = df.select_dtypes(include='number')
a.corr()
