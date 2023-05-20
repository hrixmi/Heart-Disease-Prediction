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

    # Validate age input
    if age:
        if not age.isdigit():
            st.error('Age must be a valid number.')
        else:
            age = int(age)
            if age < 18 or age > 100:
                st.error('Age must be between 18 and 100.')
    else:
        st.error('Please enter an age.')


# ...

    sex = st.selectbox('Select Sex', ['Male', 'Female'])
    cp = st.selectbox('Select Chest Pain Type', ['Typical angina', 'Atypical angina', 'Non-anginal pain', 'Asymptomatic'])
    
    
    trestbps = st.text_input('Enter Resting Blood Pressure')
    # Validate resting blood pressure input
    if trestbps:
        if not trestbps.isdigit():
            st.error('Resting blood pressure must be a valid number.')
        else:
            trestbps = int(trestbps)
            if trestbps < 60 or trestbps > 300:
                st.error('Resting blood pressure must be between 60 and 300 mmHg.')
    else:
        st.error('Please enter a resting blood pressure.')
    
    
    
    chol = st.text_input('Enter Cholesterol Level')
    # Validate cholesterol level input
    if chol:
        if not chol.isdigit():
            st.error('Cholesterol level must be a valid number.')
        else:
            chol = int(chol)
            if chol < 50 or chol > 500:
                st.error('Cholesterol level must be between 50 and 500.')
    else:
        st.error('Please enter a cholesterol level.')
    
    
    
    
    fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', ['Yes', 'No'])
    restecg = st.selectbox('Select Resting Electrocardiographic Results', ['Normal', 'Having ST-T wave abnormality', 'Showing probable or definite left ventricular hypertrophy'])
    
    
    thalach = st.text_input('Enter Maximum Heart Rate Achieved')
    # Validate maximum heart rate achieved input
    if thalach:
        if not thalach.isdigit():
            st.error('Maximum heart rate achieved must be a valid number.')
        else:
            thalach = int(thalach)
            if thalach < 0 or thalach > 300:
                st.error('Maximum heart rate achieved must be between 0 and 300.')
    else:
        st.error('Please enter a maximum heart rate achieved.')
    
    
    
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
    st.write('Version 1.3 | Last updated: May 2023 | Created by - Group 28')
    st.write('[View source code]()')
    
if __name__ == '__main__':
    main()
