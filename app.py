import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
# Set page configuration
st.set_page_config(page_title="MediPredict by Wazingwa",
                   layout="wide",
                   page_icon="❤️")
# **Add a logo image** at the top of the app
# Make sure to save the logo image file in your working directory
st.image("logo.png", width=300)  # Adjust the image size as needed

    
# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models

diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open(f'{working_dir}/saved_models/heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open(f'{working_dir}/saved_models/parkinsons_model.sav', 'rb'))



# sidebar for navigation
with st.sidebar:
    selected = option_menu('MediPredict',

                           ['Home', 'Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction','About', 'BMI Calculator'], #'Breast Cancer'],
                           menu_icon='hospital-fill',
                           icons=['home', 'activity', 'heart', 'person', 'activity','heart','activity'],
                           default_index=0)

if selected == 'About':

    # Page title
    st.title('About Me')
    st.image('IMG-20240113-WA0032~2.jpg', width = 300)

    # Personal details
    st.header('Personal Details')
    st.write("**Name:** Wazingwa Mugala")
    st.write("**Location:** Chililabombwe")
    st.write("**Education:** BSc. Computer Science @The Copperbelt University")
    st.write("**Interests:** AI, ML, Software Development")

    # Contact details
    st.header('Contact Details')
    st.write("**Email:** wazingwamugala90@gmail.com")
    st.write("**Phone:** +260763299861")
    st.write("**LinkedIn:** [Your LinkedIn Profile](your_linkedin_profile_url)")

    # Project descriptions with emojis
    st.header('My Projects')

    st.markdown("""
    ### Real-Time Facial Detection 🧑‍💻
    Detects faces of those who have attended a class. This project uses computer vision techniques to enhance classroom attendance tracking.

   

    ### Diabetes Prediction 🩸📈
    Predicts the likelihood of diabetes based on user input data. The project utilizes machine learning algorithms to provide health insights.
    """)

if selected == 'Home':
    st.markdown("""
    <h1 style="text-align: center;">Disease Prediction Using Machine Learning</h1>
    """, unsafe_allow_html=True)

    
   
    st.image('c.png')

    st.markdown("""
    <h4 style="text-align: center;">Harnessing the power of Machine Learning in Healthcare</h4>
    """, unsafe_allow_html=True)
    
    st.image('indo.jpg')
 

#The BMI Calculator App
if selected == 'BMI Calculator':
    st.title("BMI Calculator App📈")
    height = st.slider("Enter your height in cm : ", 100,250,175)
    weight = st.slider("Enter your weight in Kg: ",40,200,70)
    bmi = weight / ((height/100) ** 2)
    st.write(f"Your BMI is {bmi:.2f}")
    #BMI categories!
    st.write("### BMI Categories ###")
    st.write("- Underweight: BMI less than 18.5")
    st.write("- Normal weight: BMI between 18.5 and 24.9")
    st.write("- Overweight: BMI between 25 and 29.9")
    st.write("- Obesity: BMI 30 or greater")
    

    
    
    
    


# Diabetes Prediction Page
if selected == 'Diabetes Prediction':

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

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

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

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)
