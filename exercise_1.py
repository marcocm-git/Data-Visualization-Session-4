import streamlit as st

st.title('Exercise 1')

st.write('Press the Button?')

pressed = st.button('Tempting Button')

if pressed:
    st.write('Silly Monkey')
    st.image('monkey.jpg')