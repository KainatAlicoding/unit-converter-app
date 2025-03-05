import streamlit as st

def convert_units(value, from_unit, to_unit, conversion_dict):
    if from_unit in conversion_dict and to_unit in conversion_dict:
        return value * (conversion_dict[to_unit] / conversion_dict[from_unit])
    return None

st.title("Unit Converter App")

# Conversion dictionaries
length_units = {"Meters": 1, "Kilometers": 0.001, "Centimeters": 100, "Inches": 39.3701, "Feet": 3.28084}
weight_units = {"Kilograms": 1, "Grams": 1000, "Pounds": 2.20462, "Ounces": 35.274}
temp_units = {"Celsius": 1, "Fahrenheit": 1.8, "Kelvin": 1}

type_of_conversion = st.selectbox("Select conversion type", ["Length", "Weight", "Temperature"])

if type_of_conversion == "Length":
    from_unit = st.selectbox("From", length_units.keys())
    to_unit = st.selectbox("To", length_units.keys())
    value = st.number_input("Enter value", min_value=0.0, step=0.1)
    if st.button("Convert"):
        result = convert_units(value, from_unit, to_unit, length_units)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif type_of_conversion == "Weight":
    from_unit = st.selectbox("From", weight_units.keys())
    to_unit = st.selectbox("To", weight_units.keys())
    value = st.number_input("Enter value", min_value=0.0, step=0.1)
    if st.button("Convert"):
        result = convert_units(value, from_unit, to_unit, weight_units)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif type_of_conversion == "Temperature":
    from_unit = st.selectbox("From", temp_units.keys())
    to_unit = st.selectbox("To", temp_units.keys())
    value = st.number_input("Enter value", step=0.1)
    if st.button("Convert"):
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            result = (value * 9/5) + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            result = (value - 32) * 5/9
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            result = value + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            result = value - 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            result = (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            result = (value - 273.15) * 9/5 + 32
        else:
            result = value
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
