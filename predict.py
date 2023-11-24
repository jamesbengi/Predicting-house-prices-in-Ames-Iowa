import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('model.pk','rb') as file:
        data=pickle.load(file)
        
    return data
data=load_model()
regressor=data['model']
def make_prediction(model,features):
    prediction=model.predict(features.reshape(1,-1))
    return prediction[0]
#prediction page
def prediction_page():
    OverallQual=st.slider('Overall material and finish quality',0,10)
    TotRmsAbvGrd=st.slider('Total rooms above grade (does not include bathrooms)',0,14)
    GrLivArea=st.number_input('Above grade (ground) living area square feet')
    TotalBsmtSF=st.number_input('Total square feet of basement area')
    GarageArea=st.number_input('Size of garage in square feet')
    BsmtFinSF1=st.number_input('Type 1 finished square feet')
    LotArea=st.number_input('Lot size in square feet')
    YearBuilt=st.number_input('Original construction Year',min_value=1900, max_value=2100, step=1)
    YearRemodAdd=st.number_input('Remodel Year',min_value=1900, max_value=2100, step=1)
    click=st.button('Predict')
    if click:
        X=np.array([ [OverallQual, GrLivArea,TotalBsmtSF,BsmtFinSF1,GarageArea,
        LotArea,YearBuilt,TotRmsAbvGrd,YearRemodAdd]])
        price = regressor.predict(X)
        st.subheader(f"The estimated House price  is ${price[0]:.2f}")








