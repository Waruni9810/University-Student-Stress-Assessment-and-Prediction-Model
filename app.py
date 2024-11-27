import warnings
warnings.filterwarnings('ignore')

import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('stress_level_model.pkl') 

# Streamlit app title
st.title('Stress Level Prediction for University Students')

# Streamlit Input Fields for General Questions
st.header('Enter your details')

# Map text input to numeric values for model prediction
input_map = {
    "Very Low": 1,
    "Low": 2,
    "Moderate": 3,
    "High": 4,
    "Very High": 5,
    "Very Dissatisfied": 1,
    "Dissatisfied": 2,
    "Neutral": 3,
    "Satisfied": 4,
    "Very Satisfied": 5,
    "Never": 1,
    "Rarely": 2,
    "Sometimes": 3,
    "Often": 4,
    "Always": 5,
    "Living with Parents": 1,
    "Living with Roommates": 2,
    "Living Alone": 3,
    "Not At All": 1,
    "Slightly": 2,
    "Moderately": 3,
    "A Lot": 4,
    "Extremely": 5,
    "Very Poor": 1,
    "Poor": 2,
    "Neutral": 3,
    "Good": 4,
    "Very Good": 5,
    "Very Few": 1,
    "Few": 2,
    "Moderate": 3,
    "Many": 4,
    "Very Many": 5,
}

# Collect user inputs using selectboxes and sliders (mapped to numeric values)
time_for_study = st.selectbox('How much time do you have for studying and assignments?', ["Very Low", "Low", "Moderate", "High", "Very High"])
academic_satisfaction = st.selectbox('How satisfied are you with your current academic performance?', ["Very Dissatisfied", "Dissatisfied", "Neutral", "Satisfied", "Very Satisfied"])
impact_of_challenges = st.selectbox('How much do challenges affect your academic performance?', ["Not At All", "Slightly", "Moderately", "A Lot", "Extremely"])
seek_help_when_stressed = st.selectbox('How often do you seek help when stressed?', ["Never", "Rarely", "Sometimes", "Often", "Always"])
family_issues_impact = st.selectbox('Do family issues affect your academic performance?', ["Not At All", "Slightly", "Moderately", "A Lot", "Extremely"])
career_thoughts = st.selectbox('How often do you think about your future career prospects?', ["Never", "Rarely", "Sometimes", "Often", "Always"])
stress_impact_on_performance = st.selectbox('How much does stress affect your academic performance?', ["Not At All", "Slightly", "Moderately", "A Lot", "Extremely"])
relationship_conflicts = st.selectbox('Do you experience any conflicts in your relationships?', ["Never", "Rarely", "Sometimes", "Often", "Always"])
skip_meals = st.selectbox('How often do you skip meals?', ["Never", "Rarely", "Sometimes", "Often", "Always"])
diet_balance = st.selectbox('How balanced is your diet?', ["Very Poor", "Poor", "Neutral", "Good", "Very Good"])
social_life_satisfaction = st.selectbox('How satisfied are you with your social life and friendships?', ["Very Dissatisfied", "Dissatisfied", "Neutral", "Satisfied", "Very Satisfied"])
sleep_quality = st.selectbox('How would you rate your sleep quality and duration?', ["Very Poor", "Poor", "Neutral", "Good", "Very Good"])
family_visits = st.selectbox('How frequently do you visit your family during the academic term?', ["Never", "Rarely", "Sometimes", "Often", "Always"])
study_hours_per_week = st.selectbox('How many hours per week do you spend on studying?', ["Very Few", "Few", "Moderate", "Many", "Very Many"])
smartphone_usage = st.selectbox('How often do you use your smartphone for non-academic purposes during study hours?', ["Never", "Rarely", "Sometimes", "Often", "Always"])
living_situation = st.selectbox('What is your current living situation?', ["Living with Parents", "Living with Roommates", "Living Alone"])

# Collect inputs for PSS questions
st.subheader("Answer the 10 Perceived Stress Scale (PSS) Questions")
pss_1 = st.slider('In the last month, how often have you been upset because of something that happened unexpectedly? (0-4)', 0, 4)
pss_2 = st.slider('In the last month, how often have you felt that you were unable to control the important things in your life? (0-4)', 0, 4)
pss_3 = st.slider('In the last month, how often have you felt nervous and “stressed”? (0-4)', 0, 4)
pss_4 = st.slider('In the last month, how often have you felt confident about your ability to handle your personal problems? (0-4)', 0, 4)
pss_5 = st.slider('In the last month, how often have you felt that things were going your way? (0-4)', 0, 4)
pss_6 = st.slider('In the last month, how often have you found that you could not cope with all the things that you had to do? (0-4)', 0, 4)
pss_7 = st.slider('In the last month, how often have you been able to control irritations in your life? (0-4)', 0, 4)
pss_8 = st.slider('In the last month, how often have you felt that you were on top of things? (0-4)', 0, 4)
pss_9 = st.slider('In the last month, how often have you been angered because of things that were outside of your control? (0-4)', 0, 4)
pss_10 = st.slider('In the last month, how often have you felt difficulties were piling up so high that you could not overcome them? (0-4)', 0, 4)

# Calculate the total score for the PSS questions
pss_total = (pss_1 + pss_2 + pss_3 + pss_4 + pss_5 + pss_6 + pss_7 + pss_8 + pss_9 + pss_10) / 10

# Add a button to trigger the prediction
if st.button('Predict Stress Level'):
    # Prepare the data for prediction
    user_input = pd.DataFrame({
        '3.Do you feel you have enough time to complete your assignments and study for exams?': [input_map[time_for_study]],
        '5.How satisfied are you with your current academic performance?': [input_map[academic_satisfaction]],
        '2. How have these challenges impacted your academic performance?': [input_map[impact_of_challenges]],
        '5. How often do you seek help or advice from others when stressed?': [input_map[seek_help_when_stressed]],
        '5. Do family issues (e.g., conflicts, responsibilities) affect your academic performance?': [input_map[family_issues_impact]],
        '4. How often do you think about your future career prospects?': [input_map[career_thoughts]],
        '6. Do you feel that stress has affected your academic performance?': [input_map[stress_impact_on_performance]],
        '5. Do you experience any conflicts or pressures in your relationships?': [input_map[relationship_conflicts]],
        '5. Do you often skip meals?': [input_map[skip_meals]],
        '4. How balanced is your diet?': [input_map[diet_balance]],
        '4. How satisfied are you with your social life and friendships?': [input_map[social_life_satisfaction]],
        '2. How would you rate your sleep quality and duration?': [input_map[sleep_quality]],
        '4. How frequently do you visit your family during the academic term?': [input_map[family_visits]],
        '1. How many hours per week do you typically spend on coursework and studying?': [input_map[study_hours_per_week]],
        '2. How often do you use your smartphone for non-academic purposes during study hours?': [input_map[smartphone_usage]],
        '1. What is your current living situation?': [input_map[living_situation]],
        'PSS_Total': [pss_total]  # Using the calculated PSS_Total
    })
    
    # Predict the stress level using the model
    prediction = model.predict(user_input)
    
    # Display the result
    if prediction[0] == 'Low':
        st.write("### Predicted Stress Level: **Low**")
    elif prediction[0] == 'Moderate':
        st.write("### Predicted Stress Level: **Moderate**")
    else:
        st.write("### Predicted Stress Level: **High**")
