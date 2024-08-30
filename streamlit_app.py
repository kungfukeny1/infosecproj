import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('model.pkl', 'rb'))  # Load the model

col0, col1, col2, col3, col4, col5, col6 = st.columns(7)  # Create columns

with col0:
    st.write('')  # Empty column
with col1:
    st.write('')  # Empty column
with col2:
    st.write('')  # Empty column
with col3:
    st.title("age")  # Display title
with col4:
    st.write('')  # Empty column
with col5:
    st.write('')  # Empty column
with col6:
    st.write('')  # Empty column

col7, col8, col9 = st.columns(3)  # Create 3 columns

with col7:
    st.write('')  # Empty column
with col8:
    st.markdown("<h6 style='text-align: center;'>A simple web app to predict annual salary</h6>", unsafe_allow_html=True)  # Display markdown text
with col9:
    st.write('')  # Empty column

# Define lists of options for the user to select from
gen_list = ["Female", "Male"]  # List of genders
edu_list = ["Bachelor's", "Master's", "PhD"]  # List of education levels
job_list = ["Director of Marketing", "Director of Operations", "Senior Data Scientist", "Senior Financial Analyst", "Senior Software Engineer"]  # List of job titles
job_idx = [0, 1, 10, 11, 20]  # List of job indices

# Create interactive widgets for the user to input their data
gender = st.radio('Pick your gender', gen_list)  # Select gender
age = st.slider('Pick your age', 21, 55)  # Select age
education = st.selectbox('Pick your education level', edu_list)  # Select education level
job = st.selectbox('Pick your job title', job_list)  # Select job title
experience = st.slider('Pick your years of experience', 0.0, 25.0, 0.0, 0.5, "%1f")  # Select experience

# Create 5 more columns for layout purposes
col10, col11, col12, col13, col14 = st.columns(5)  # Create columns

# Use the columns to create an empty layout and display a button
with col10:
    st.write('')  # Empty column
with col11:
    st.write('')  # Empty column
with col12:
    predict_btn = st.button('Predict Salary')  # Create predict button
with col13:
    st.write('')  # Empty column
with col14:
    st.write('')  # Empty column

# Check if the button has been clicked
if predict_btn:  # Check if button clicked
    # Convert the user input to numerical values
    inp1 = int(age)  # Convert age to int
    inp2 = float(experience)  # Convert experience to float
    inp3 = int(job_idx[job_list.index(job)])  # Convert job to int
    inp4 = int(edu_list.index(education))  # Convert education to int
    inp5 = int(gen_list.index(gender))  # Convert gender to int
    
    # Create a list of input values
    X = [inp1, inp2, inp3, inp4, inp5]  # Create input list
    
    # Use the model to predict the salary
    salary = model.predict([X])  # Predict salary
    
    # Create 3 more columns for layout purposes
    col15, col16, col17 = st.columns(3)  # Create columns
    
    # Use the columns to display the predicted salary
    with col15:
        st.write('')  # Empty column
    with col16:
        st.text(f"Estimated salary: ${int(salary[0])}")  # Display predicted salary
    with col17:
        st.write('')  # Empty column