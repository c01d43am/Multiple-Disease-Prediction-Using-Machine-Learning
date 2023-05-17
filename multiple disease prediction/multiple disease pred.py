# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 10:22:07 2023

@author: ss630
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open('C:/Users/Pawan/Desktop/multiple disease prediction/saved models/diabetes_model.pkl','rb'))

heart_disease_model = pickle.load(open('C:/Users/Pawan/Desktop/multiple disease prediction/saved models/heart.pkl','rb'))

liver_model = pickle.load(open('C:/Users/Pawan/Desktop/multiple disease prediction/saved models/liver.pkl', 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Liver Disease Prediction'],
                          icons=['activity','heart','cat'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    
    

# Liver Prediction Page
if (selected == "Liver Disease Prediction"):
    
    # page title
    st.title("Liver Disease Prediction using ML")
    
    col1, col2, col3 = st.columns(3)  
    
    with col1:
        Age = st.text_input('Age')
        
    with col2:
        Gender = st.text_input('Gender')
        
    with col3:
        Total_Bilirubin= st.text_input('Total_Bilirubin')
        
    with col1:
        Direct_Bilirubin = st.text_input('Direct_Bilirubin')
        
    with col2:
        Alkaline_Phosphotase = st.text_input('Alkaline_Phosphotase')
        
    with col3:
        Alamine_Aminotransferase = st.text_input('Alamine_Aminotransferase')
        
    with col1:
        Aspartate_Aminotransferase = st.text_input('Aspartate_Aminotransferase')
        
    with col2:
        Total_Protiens = st.text_input('Total_Protiens')
        
    with col3:
        Albumin= st.text_input('Albumin')
        
    with col1:
        Albumin_and_Globulin_Ratio = st.text_input('Albumin_and_Globulin_Ratio')
        
    
        
    
    
    # code for Prediction
    liver_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Liver Test Result"):
        liver_prediction = liver_model.predict([[Age,Gender,Total_Bilirubin,Direct_Bilirubin,Alkaline_Phosphotase,Alamine_Aminotransferase,Aspartate_Aminotransferase,Total_Protiens,Albumin,Albumin_and_Globulin_Ratio]])                          
        
        if (liver_prediction[0] == 1):
          liver_diagnosis = "The person has liver disease"
        else:
          liver_diagnosis = "The person does not have liver disease"
        
    st.success(liver_diagnosis)