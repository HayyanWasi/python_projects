import streamlit as st

st.title(" Length Unit Converter")


unit = st.selectbox(
    "Select input unit:",
    ["Meter", "Centimeter", "Millimeter", "Kilometer", 
     "Inch", "Foot", "Yard", "Mile"]
)


if unit == "Meter":
    user_input = st.number_input("Enter number to convert from meters")
    value = float(user_input)
    
    st.subheader("Conversion Results:")
    st.text(f"{value * 100} centimeters")
    st.text(f"{value * 1000} millimeters")
    st.text(f"{value / 1000} kilometers")
    st.text(f"{value * 39.37} inches")
    st.text(f"{value * 3.281} feet")
    st.text(f"{value * 1.094} yards")
    st.text(f"{value / 1609} miles")

elif unit == "Centimeter":
    user_input = st.number_input("Enter number to convert from centimeters")
    value = float(user_input)
    
    st.subheader("Conversion Results:")
    st.text(f"{value / 100} meters")
    st.text(f"{value * 10} millimeters")
    st.text(f"{value / 100000} kilometers")
    st.text(f"{value / 2.54} inches")
    st.text(f"{value / 30.48} feet")
    st.text(f"{value / 91.44} yards")
    st.text(f"{value / 160934} miles")

elif unit == "Millimeter":
    user_input = st.number_input("Enter number to convert from millimeters")
    value = float(user_input)
    
    st.subheader("Conversion Results:")
    st.text(f"{value / 1000} meters")
    st.text(f"{value / 10} centimeters")
    st.text(f"{value / 1e6} kilometers")
    st.text(f"{value / 25.4} inches")
    st.text(f"{value / 304.8} feet")
    st.text(f"{value / 914.4} yards")
    st.text(f"{value / 1.609e6} miles")

elif unit == "Kilometer":
    user_input = st.number_input("Enter number to convert from kilometers")
    value = float(user_input)
    
    st.subheader("Conversion Results:")
    st.text(f"{value * 1000} meters")
    st.text(f"{value * 100000} centimeters")
    st.text(f"{value * 1e6} millimeters")
    st.text(f"{value * 39370} inches")
    st.text(f"{value * 3281} feet")
    st.text(f"{value * 1094} yards")
