import streamlit as st




# Add a title to your app
st.title('Sample App 1')


slider = st.slider('Number of Motors:', min_value=1, max_value=20)


select_box = st.selectbox("What type of rocket?",
    ("Solid", "Hybrid", "Liquid"))

# def calculate_square(x):
#     return x**2
# if st.button('Calculate'):
#     st.write(calculate_square(2))

