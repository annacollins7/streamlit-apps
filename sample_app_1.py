import streamlit as st




# Add a title to your app
st.title('Sample App 1')


number_of_motors = st.slider('Number of Motors:', min_value=1, max_value=20)

st.write(str(number_of_motors))

motor_type = st.selectbox("What type of rocket?",
    ("Solid", "Hybrid", "Liquid"))


# Solid case
if motor_type is "Solid":
    st.write("Need to electrocute it")

# Hybrid case


# Liquid case





# def calculate_square(x):
#     return x**2

# if st.button('Calculate'):
#     st.write(calculate_square(2))
#     print(calculate_square(2))

