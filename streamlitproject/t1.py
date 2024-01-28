# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pickle 
import streamlit as st

# تحميل النموذج المدرب
loaded_model = pickle.load(open('C:/Users/LENOVO/Desktop/trained_model.sav', 'rb'))

def diabetes (input_data):
    #input_data = (5,166,72,19,175,25.8,0.587,51)

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)


    if (prediction[0] == 0):
      return('The person is not diabetic')
    else:
      return('The person is diabetic')
    return (prediction)
def main():
    
      
      # the name of the websit
    st.title('heart')
   

    
    Thall = st.number_input('Enter the number of   Thall: ',step=1,placeholder="insert ur num")
    Sex = st.selectbox('Select the sex:', ['Man', 'Woman'])
    Cp = st.number_input('Enter the Cp : ',step=1,placeholder="insert ur num")
    Trtbps = st.number_input('Enter the blood Trtbps: ',step=1,placeholder="insert ur num")
    Chol = st.number_input('Enter the  Chol: ',step=1,placeholder="insert ur num")
    Thalachh = st.number_input('Enter the Thalachh: ',step=1,placeholder="insert ur num")
    Oldpeak = st.number_input('Enter the Oldpeak: ',step=1,placeholder="insert ur num")
    DiabetesPedigreeFunction = st.number_input('Enter the diabetes pedigree function: ',step=1,placeholder="insert ur num")
    Age = st.number_input('Enter the age: ',step=1,placeholder="insert ur num")
  

    
    # code for pediction 
    dignosis = ''
    # creating a button for perdiction
    if st.button('Diabetes test Result'):
        dignosis = diabetes([Pregnancies,Sex,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
        
        
    st.success(dignosis)
    
if __name__ == '__main__':
    main()