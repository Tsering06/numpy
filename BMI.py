import streamlit as st

st.title("Body Mass Index Calculator")

weight = st.number_input('Enter your Weight (KG):')
feet = st.number_input('Enter height (feet):', min_value=0, step=1)
inches = st.number_input('Enter additional height (inches):', min_value=0, max_value=11, step=1)

height = feet + (inches / 12)
btn = st.button('Calculate BMI')

if btn:
    bmi = weight/((height/3.28)**2)
    if bmi<16:
        st.eror('You are extremely underweight!')
    elif bmi>=16 and bmi<18.5:
        st.warning('You are underweight!')
    elif bmi>=18.5 and bmi<25:
        st.success('Congrats you are Healthy!')
    elif bmi>=25 and bmi<30:
        st.info('You are over weight')
    elif bmi>=30:
        st.error('You are extremely overweight')