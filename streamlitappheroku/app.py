import pickle
from pathlib import Path

import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd


st.set_page_config(page_title='Multiple Disease Prediction System', page_icon='🩺')


def load_model(filename):
    model_path = Path(__file__).resolve().parent / filename
    with model_path.open('rb') as model_file:
        return pickle.load(model_file)


diabetes_model = load_model('diabetes_model.sav')
heart_disease_model = load_model('heart_disease_model.sav')
parkinsons_model = load_model('parkinsons_model.sav')

hide_deploy_button = """
    <style>
        .stAppDeployButton {
            display: none !important;
        }
    </style>
"""

st.markdown(hide_deploy_button, unsafe_allow_html=True)

# sidebar for navigation
with st.sidebar:

    selected = option_menu('Multiple Disease Prediction System',

                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction'],
                          icons=['activity','heart','person'],
                          default_index=0)


# Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    # Page Title
    st.title('Diabetes Prediction using ML')

    # Input Fields with Proper Data Handling
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.number_input('Number of Pregnancies', min_value=0, max_value=20, step=1)
    with col2:
        Glucose = st.number_input('Glucose Level', min_value=0, max_value=300, step=1)
    with col3:
        BloodPressure = st.number_input('Blood Pressure Value', min_value=0, max_value=200, step=1)

    with col1:
        SkinThickness = st.number_input('Skin Thickness Value', min_value=0, max_value=100, step=1)
    with col2:
        Insulin = st.number_input('Insulin Level', min_value=0, max_value=1000, step=1)
    with col3:
        BMI = st.number_input('BMI Value', min_value=0.0, max_value=100.0, step=0.1)

    with col1:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function Value', min_value=0.0, max_value=3.0, step=0.01)
    with col2:
        Age = st.number_input('Age of the Person', min_value=1, max_value=120, step=1)

    # Prediction Output
    diab_diagnosis = ''

    # Prediction Button
    if st.button('Diabetes Test Result'):
        try:
            # Convert inputs into numpy array
            input_data = pd.DataFrame(
                [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]],
                columns=diabetes_model.feature_names_in_,
            )

            # Model Prediction
            diab_prediction = diabetes_model.predict(input_data)

            # Display Result
            if diab_prediction[0] == 1:
                diab_diagnosis = '🚨 The person is diabetic.'
            else:
                diab_diagnosis = '✅ The person is not diabetic.'

            st.success(diab_diagnosis)

        except Exception as e:
            st.error(f"An error occurred: {e}")




# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # Page Title
    st.title('Heart Disease Prediction using ML')

    # Input Fields with Proper Data Handling
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input('Age', min_value=1, max_value=120, step=1)
    with col2:
        sex = st.selectbox('Sex', options=[0, 1], format_func=lambda x: 'Male' if x == 1 else 'Female')
    with col3:
        cp = st.selectbox('Chest Pain Type', options=[0, 1, 2, 3])

    with col1:
        trestbps = st.number_input('Resting Blood Pressure', min_value=50, max_value=250, step=1)
    with col2:
        chol = st.number_input('Serum Cholesterol (mg/dl)', min_value=100, max_value=600, step=1)
    with col3:
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', options=[0, 1])

    with col1:
        restecg = st.selectbox('Resting Electrocardiographic results', options=[0, 1, 2])
    with col2:
        thalach = st.number_input('Maximum Heart Rate Achieved', min_value=50, max_value=250, step=1)
    with col3:
        exang = st.selectbox('Exercise Induced Angina', options=[0, 1])

    with col1:
        oldpeak = st.number_input('ST Depression Induced by Exercise', min_value=0.0, max_value=10.0, step=0.1)
    with col2:
        slope = st.selectbox('Slope of Peak Exercise ST Segment', options=[0, 1, 2])
    with col3:
        ca = st.number_input('Number of Major Vessels Colored by Fluoroscopy', min_value=0, max_value=4, step=1)

    with col1:
        thal = st.selectbox('Thalassemia Type', options=[0, 1, 2, 3])

    # Prediction Output
    heart_diagnosis = ''

    # Prediction Button
    if st.button('Heart Disease Test Result'):
        try:
            # Model Prediction
            input_data = pd.DataFrame(
                [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]],
                columns=heart_disease_model.feature_names_in_,
            )
            heart_prediction = heart_disease_model.predict(input_data)

            # Display Result
            if heart_prediction[0] == 1:
                heart_diagnosis = '🚨 The person has heart disease.'
            else:
                heart_diagnosis = '✅ The person does not have heart disease.'

            st.success(heart_diagnosis)

        except Exception as e:
            st.error(f"An error occurred: {e}")




# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

    # Page Title
    st.title("🧠 Parkinson's Disease Prediction using ML")

    # Input Fields
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.number_input('MDVP:Fo(Hz)', min_value=0.0, step=0.01)
    with col2:
        fhi = st.number_input('MDVP:Fhi(Hz)', min_value=0.0, step=0.01)
    with col3:
        flo = st.number_input('MDVP:Flo(Hz)', min_value=0.0, step=0.01)
    with col4:
        Jitter_percent = st.number_input('MDVP:Jitter(%)', min_value=0.0, step=0.0001, format="%.5f")
    with col5:
        Jitter_Abs = st.number_input('MDVP:Jitter(Abs)', min_value=0.0, step=0.0001, format="%.5f")

    with col1:
        RAP = st.number_input('MDVP:RAP', min_value=0.0, step=0.0001, format="%.5f")
    with col2:
        PPQ = st.number_input('MDVP:PPQ', min_value=0.0, step=0.0001, format="%.5f")
    with col3:
        DDP = st.number_input('Jitter:DDP', min_value=0.0, step=0.0001, format="%.5f")
    with col4:
        Shimmer = st.number_input('MDVP:Shimmer', min_value=0.0, step=0.0001, format="%.5f")
    with col5:
        Shimmer_dB = st.number_input('MDVP:Shimmer(dB)', min_value=0.0, step=0.01)

    with col1:
        APQ3 = st.number_input('Shimmer:APQ3', min_value=0.0, step=0.0001, format="%.5f")
    with col2:
        APQ5 = st.number_input('Shimmer:APQ5', min_value=0.0, step=0.0001, format="%.5f")
    with col3:
        APQ = st.number_input('MDVP:APQ', min_value=0.0, step=0.0001, format="%.5f")
    with col4:
        DDA = st.number_input('Shimmer:DDA', min_value=0.0, step=0.0001, format="%.5f")
    with col5:
        NHR = st.number_input('NHR', min_value=0.0, step=0.0001, format="%.5f")

    with col1:
        HNR = st.number_input('HNR', min_value=0.0, step=0.01)
    with col2:
        RPDE = st.number_input('RPDE', min_value=0.0, step=0.0001, format="%.5f")
    with col3:
        DFA = st.number_input('DFA', min_value=0.0, step=0.0001, format="%.5f")
    with col4:
        spread1 = st.number_input('spread1', step=0.0001, format="%.5f")
    with col5:
        spread2 = st.number_input('spread2', step=0.0001, format="%.5f")

    with col1:
        D2 = st.number_input('D2', min_value=0.0, step=0.0001, format="%.5f")
    with col2:
        PPE = st.number_input('PPE', min_value=0.0, step=0.0001, format="%.5f")

    # Prediction Output
    parkinsons_diagnosis = ""

    # Prediction Button
    if st.button("🧪 Parkinson's Test Result"):
        try:
            # Convert inputs to a NumPy array
            input_data = pd.DataFrame(
                [[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB,
                  APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]],
                columns=parkinsons_model.feature_names_in_,
            )

            # Model Prediction
            parkinsons_prediction = parkinsons_model.predict(input_data)

            # Display Result
            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = "🚨 The person **has** Parkinson's disease."
            else:
                parkinsons_diagnosis = "✅ The person **does not have** Parkinson's disease."

            st.success(parkinsons_diagnosis)

        except Exception as e:
            st.error(f"An error occurred: {e}")
