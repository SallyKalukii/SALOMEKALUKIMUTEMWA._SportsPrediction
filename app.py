import streamlit as st
import joblib
import pandas as pd 

model_path = 'C:/Users/salome.mutemwa/Desktop/SALOMEKALUKIMUTEMWA._SportsPrediction/trained_model.pkl'


loaded_model = joblib.load(model_path)

# Title of the web app
st.title('Player Rating Prediction')

# Creating a form
with st.form(key='player_features_form'):
     
    movement_reactions = st.number_input('Movement Reactions', min_value=0, max_value=100, value=50)
    mentality_composure = st.number_input('Mentality Composure', min_value=0, max_value=100, value=50)
    potential = st.number_input('Potential', min_value=0, max_value=100, value=50)
    passing = st.number_input('Passing', min_value=0, max_value=100, value=50)
    attacking_short_passing = st.number_input('Attacking Short Passing', min_value=0, max_value=100, value=50)
    mentality_vision = st.number_input('Mentality Vision', min_value=0, max_value=100, value=50)
    international_reputation = st.number_input('International Reputation', min_value=0, max_value=100, value=50)
    skill_long_passing = st.number_input('Skill Long Passing', min_value=0, max_value=100, value=50)
    power_shot_power = st.number_input('Power Shot Power', min_value=0, max_value=100, value=50)
    physic = st.number_input('Physic', min_value=0, max_value=100, value=50)
    
    # creating a Submit button
    submit_button = st.form_submit_button(label='Submit')

# Check if the form is submitted
if submit_button:
    # Create a DataFrame for the input features
    input_features = pd.DataFrame({
        'movement_reactions': [movement_reactions],
        'mentality_composure': [mentality_composure],
        'potential': [potential],
        'passing': [passing],
        'attacking_short_passing': [attacking_short_passing],
        'mentality_vision': [mentality_vision],
        'international_reputation': [international_reputation],
        'skill_long_passing': [skill_long_passing],
        'power_shot_power': [power_shot_power],
        'physic': [physic]
    })
    prediction = loaded_model.predict(input_features)
    # Display prediction
    st.subheader('Predicted Player Rating')
    
    st.write(prediction[0])


