import numpy as np
import pickle
import streamlit as st
from PIL import Image

#loading the saved model
loaded_model=pickle.load(open('trained_model.sav','rb'))

#creating a function for Prediction

def heart_diseases_prediction(input_data):
    
    # change the input data to a numpy array
    input_data_as_numpy_array= np.asarray(input_data, dtype=float)
    
    # reshape the numpy array as we are predicting for only one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    prediction = loaded_model.predict(input_data_reshaped)
        
    if (prediction[0]==[0]):
        return('The Person does not have a Heart Disease')
    else:
        return('The Person has Heart Disease')

        
def main():

    st.set_page_config(page_title="Heart Disease Web App", page_icon=":heart:", layout="wide")
    col1, col2 = st.columns([2, 1])  
    with col1:
        st.header('Welcome to the Heart Disease Web App')
        st.subheader('Enter the details below to check if you have heart disease')
    image = Image.open("heart.png")
    with col2:
        st.image(image, width=100,output_format="auto",)
    
    #st.header('Welcome to the Heart Disease Web App')
    
    #st.write("""****""")



    #st.markdown('<style>body{background-color: #f5f5f5; font-family: Arial, sans-serif;}</style>', unsafe_allow_html=True)


    
    #getting the input data from the user
    age = st.text_input('Enter Age')
    sex = st.selectbox('Select Sex', ['Male', 'Female'])
    cp = st.selectbox('Select Chest Pain Type', ['Typical angina', 'Atypical angina', 'Non-anginal pain', 'Asymptomatic'])
    trestbps = st.text_input('Enter Resting Blood Pressure')
    chol = st.text_input('Enter Cholesterol Level')
    fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', ['Yes', 'No'])
    restecg = st.selectbox('Select Resting Electrocardiographic Results', ['Normal', 'Having ST-T wave abnormality', 'Showing probable or definite left ventricular hypertrophy'])
    thalach = st.text_input('Enter Maximum Heart Rate Achieved')
    exang = st.selectbox('Exercise Induced Angina', ['Yes', 'No'])
    oldpeak = st.text_input('Enter ST Depression')
    slope = st.selectbox('Select the slope of the peak exercise ST segment', ['Upsloping', 'Flat', 'Downsloping'])
    ca = st.text_input('Enter the number of major vessels colored by fluoroscopy')
    thal = st.selectbox('Thalassemia', ['Normal', 'Fixed defect', 'Reversable defect'])
  
    
    # Preprocess the user input
    sex = 1 if sex == 'Male' else 0
    if cp == 'Typical Angina':
        cp = 0
    elif cp == 'Atypical Angina':
        cp = 1
    elif cp == 'Non-anginal Pain':
        cp = 2
    else:
        cp = 3
    fbs = 1 if fbs == 'Yes' else 0
    if restecg == 'Normal':
        restecg = 0
    elif restecg == 'ST-T Wave Abnormality':
        restecg = 1
    else:
        restecg = 2
    exang = 1 if exang == 'Yes' else 0
    if slope == 'Upsloping':
        slope = 0
    elif slope == 'Flat':
        slope = 1
    else:
        slope = 2
   
    if thal == 'Normal':
        thal = 1
    elif thal == 'Fixed Defect':
        thal = 2
    else:
        thal = 3

    
    #code for Prediction
    
    diagnosis = ''
    
    #creating a button for Prediction
    
    if st.button('Heart Test Result'):
        data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        diagnosis = heart_diseases_prediction(data)
    
    st.write('')

    
    # display the output
    if diagnosis:
        st.success(diagnosis)
        if 'not' in diagnosis:
            st.spinner('Computing..')
            st.balloons()
       
        
    st.markdown('<hr>', unsafe_allow_html=True)
    st.write('Version 1.2 | Last updated: March 2023 | Created by Group - 28 | Guided By - Dr. Tapan Chowdhury')
    st.write('[View source code]()')
    
if __name__ == '__main__':
    main()