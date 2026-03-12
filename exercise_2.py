import streamlit as st

st.title("Exercise 2")
st.title('Temperature Converter')

unit1 = st.selectbox(
    "Unit You Want to Convert",
    ["Celsius", "Kelvin", "Farenheit"]
)

unit2 = st.selectbox(
    "Converted Unit",
    ["Celsius", "Kelvin", "Farenheit"]
)

input = st.text_input("Enter temperature:")

def temp_convert(unit1, unit2, input):
    if not input:
        return
    try:
        input = float(input)
    except ValueError:
        st.error("Please enter a valid number")
        return
    
    if unit1 == unit2:
        st.write("Same Units Selected")
    elif unit1 == "Celsius" and unit2 == "Kelvin":
        conv = input + 273.15
        st.write(f"Kelvin: {conv}")

    elif unit1 == "Celsius" and unit2 == "Farenheit":
        conv = input * 1.8 + 32
        st.write(f"Farenheit: {conv}")

    elif unit1 == "Farenheit" and unit2 == "Kelvin":
        conv = ((input-32)/(1.8)) + 273.15
        st.write(f"Kelvin: {conv}")

    elif unit1 == "Farenheit" and unit2 == "Celsius":
        conv = (input-32)/(1.8)
        st.write(f"Celsius: {conv}")

    elif unit1 == "Kelvin" and unit2 == "Celsius":
        conv = input - 273.15
        st.write(f"Celsius: {conv}")
        
    elif unit1 == "Kelvin" and unit2 == "Farenheit":
        conv = (input * 1.8 + 32) - 273.15
        st.write(f"Farenheit: {conv}")

temp_convert(unit1, unit2, input)
