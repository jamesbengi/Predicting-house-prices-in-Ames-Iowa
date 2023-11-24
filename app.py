import streamlit as st
from data import next
from predict import prediction_page
st.title('Predict House Prices in Ames Iowa')
choice=st.sidebar.selectbox('Choose what to do',['Explore','Predict'])



if choice=='Explore':
    next()
else:
    prediction_page()
    
