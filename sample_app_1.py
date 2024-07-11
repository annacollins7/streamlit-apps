import streamlit as st

# Add a title to your app
st.title('Sample App 1')


slider = st.slider('Number of Motors:', min_value=1, max_value=20)

