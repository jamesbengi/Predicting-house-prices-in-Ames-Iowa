import streamlit as st
import pandas as pd
import pickle
def next():
    data=pd.read_csv('C:/Users/User/Desktop/Data Analytics projects dataset/houses prediction/train.csv')
    st.write('Data Frame')
    st.dataframe(data.head(5))