import re
import streamlit as st

def check_password_strength(password):
    score = 0
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        st.error("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
        

    else:
        st.warning("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
        

    else:
        st.warning("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1

    else:
        st.warning("❌ Include at least one special character (!@#$%^&*).")
    
    # Strength Rating
    if score == 4:
        st.write("✅ Strong Password!")
        st.write('score = ',score)
    elif score == 3:
        st.write("⚠️ Moderate Password - Consider adding more security features.")
        st.write('score = ',score)

    else:
        st.write("❌ Weak Password - Improve it using the suggestions above.")

# Get user input
password = st.text_input("Enter your password: ",type="password" )
check_password_strength(password)