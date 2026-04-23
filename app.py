import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Page config
st.set_page_config(
    page_title="Student Performance Prediction",
    page_icon="🎓",
    layout="centered"
)

# Title
st.title("🎓 Student Performance Prediction System")

st.write("Fill student details to predict performance grade")

# Input fields

student_age = st.selectbox(
    "Student Age",
    ["18", "19-22"]
)

sex = st.selectbox(
    "Sex",
    ["Female", "Male"]
)

high_school = st.selectbox(
    "High School Type",
    ["Other", "Private", "State"]
)

scholarship = st.selectbox(
    "Scholarship",
    ["25%", "50%", "75%", "Full"]
)

additional_work = st.selectbox(
    "Additional Work",
    ["No", "Yes"]
)

sports = st.selectbox(
    "Sports Activity",
    ["No", "Yes"]
)

transport = st.selectbox(
    "Transportation",
    ["Bus", "Private", "Other"]
)

study_hours = st.slider(
    "Weekly Study Hours",
    0,
    5
)

attendance = st.selectbox(
    "Attendance",
    ["Never", "Always"]
)

reading = st.selectbox(
    "Reading Books",
    ["No", "Yes"]
)

notes = st.selectbox(
    "Taking Notes",
    ["No", "Yes"]
)

listening = st.selectbox(
    "Listening in Class",
    ["No", "Yes"]
)

project = st.selectbox(
    "Project Work",
    ["No", "Yes"]
)

# Convert inputs to numbers

age_map = {
    "18": 0,
    "19-22": 1
}

sex_map = {
    "Female": 0,
    "Male": 1
}

school_map = {
    "Other": 0,
    "Private": 1,
    "State": 2
}

scholarship_map = {
    "25%": 0,
    "50%": 1,
    "75%": 2,
    "Full": 3
}

yes_no_map = {
    "No": 0,
    "Yes": 1
}

transport_map = {
    "Bus": 0,
    "Private": 1,
    "Other": 2
}

attendance_map = {
    "Never": 0,
    "Always": 1
}

# Prediction button

if st.button("Predict Grade"):

    features = np.array([[
        age_map[student_age],
        sex_map[sex],
        school_map[high_school],
        scholarship_map[scholarship],
        yes_no_map[additional_work],
        yes_no_map[sports],
        transport_map[transport],
        study_hours,
        attendance_map[attendance],
        yes_no_map[reading],
        yes_no_map[notes],
        yes_no_map[listening],
        yes_no_map[project]
    ]])

    prediction = model.predict(features)

    grades = {
        0: "AA",
        1: "BA",
        2: "BB",
        3: "CB",
        4: "CC",
        5: "DC",
        6: "DD",
        7: "Fail"
    }

    st.success(f" Predicted Grade: {grades[prediction[0]]}")