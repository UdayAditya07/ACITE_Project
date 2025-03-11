import streamlit as st
import pickle
st.set_page_config(page_title="Disease Prediction", page_icon="⚕️")
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# models = {
#     'diabetes': pickle.load(open('Models/diabetes_model.sav', 'rb')),
#     'heart_disease': pickle.load(open('Models/heart_disease_model.sav', 'rb')),
#     'parkinsons': pickle.load(open('Models/parkinsons_model.sav', 'rb')),
#     'lung_cancer': pickle.load(open('Models/lungs_disease_model.sav', 'rb')),
#     'thyroid': pickle.load(open('Models/Thyroid_model.sav', 'rb'))
# }

selected = st.selectbox(
    'Select a Disease to Predict',
    ['Diabetes Prediction',
     'Heart Disease Prediction',
     'Parkinsons Prediction',
     'Lung Cancer Prediction',
     'Hypo-Thyroid Prediction']
)

def display_input(label, tooltip, key, type="text"):
    if type == "text":
        return st.text_input(label, key=key, help=tooltip)
    elif type == "number":
        return st.number_input(label, key=key, help=tooltip, step=1)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes')
    st.write("Enter the following details to predict diabetes:")

    Pregnancies = display_input('Number of Pregnancies', 'Enter number of times pregnant', 'Pregnancies', 'number')
    Glucose = display_input('Glucose Level', 'Enter glucose level', 'Glucose', 'number')
    BloodPressure = display_input('Blood Pressure value', 'Enter blood pressure value', 'BloodPressure', 'number')
    SkinThickness = display_input('Skin Thickness value', 'Enter skin thickness value', 'SkinThickness', 'number')
    Insulin = display_input('Insulin Level', 'Enter insulin level', 'Insulin', 'number')
    BMI = display_input('BMI value', 'Enter Body Mass Index value', 'BMI', 'number')
    DiabetesPedigreeFunction = display_input('Diabetes Pedigree Function value', 'Enter diabetes pedigree function value', 'DiabetesPedigreeFunction', 'number')
    Age = display_input('Age of the Person', 'Enter age of the person', 'Age', 'number')

    # diab_diagnosis = ''
    # if st.button('Diabetes Test Result'):
    #     diab_prediction = models['diabetes'].predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
    #     diab_diagnosis = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'
    #     st.success(diab_diagnosis)