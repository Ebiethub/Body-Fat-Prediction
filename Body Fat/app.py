import streamlit as st
import pandas as pd
import pickle




pipe = pickle.load(open('BodyFatUp.pkl', 'rb'))

st.title('Body Fat Prediction')



col1, col2, col3 = st.columns(3)

with col1:
    density = st.number_input('Density')

with col2:
    abdomen = st.number_input('Abdomen')

with col3:
    chest = st.number_input('Chest')


col1, col2 = st.columns(2)

with col1:
    weight = st.number_input('Weight')

with col2:
    hip = st.number_input('Hip')

if st.button('Predict Probability'):

    input_features = [[density, abdomen, chest, weight, hip]]

    prediction = pipe.predict(input_features)[0].round(2)

    # <p class="big-font">Hello World !!</p>', unsafe_allow_html=True

    st.title('Percentage of Body Fat Estimated is : ' + str(prediction)+'%')

