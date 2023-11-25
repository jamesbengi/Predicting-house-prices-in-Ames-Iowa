import streamlit as st
import pandas as pd
import pickle
def next():
    data=pd.read_csv('/jamesbengi/Predicting-house-prices-in-Ames-Iowa/blob/master/train.csv')
    st.write('Data Frame')
    st.dataframe(data.head(5))