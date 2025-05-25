import streamlit as st
import hashlib
from cryptography.fernet import Fernet


KEY = Fernet.generate_key()
cipher = Fernet(KEY)


if 'vault' not in st.session_state:
    st.session_state.vault = {}
    
if 'wrong_tries' not in st.session_state:
    st.session_state.wrong_tries = 0


def make_hash(secret):
    return hashlib.sha256(secret.encode()).hexdigest()

def lock_message(message, secret):
    return cipher.encrypt(message.encode()).decode()

def unlock_message(locked_message, secret):
    try:
        return cipher.decrypt(locked_message.encode()).decode()
    except:
        return None


st.title("Secret Keeper Box")
st.sidebar.header("Menu")


pages = ["Home", "Save Secret", "Open Secret", "Emergency Entry"]
page = st.sidebar.selectbox("Go to", pages)


if page == "Home":
    st.write("""
    Welcome to Secret Keeper!
    * Save secrets with passwords
    * Retrieve them later
    * 3 wrong tries lock the system
    """)


elif page == "Save Secret":
    st.header("Save Your Secret")
    
    user_text = st.text_area("Type your secret here:")
    user_password = st.text_input("Create a password:", type="password")
    
    if st.button("Lock It!"):
        if user_text and user_password:
       
            password_hash = make_hash(user_password)
            
          
            encrypted = lock_message(user_text, user_password)
            
           
            st.session_state.vault[encrypted] = {
                "locked_message": encrypted,
                "password_hash": password_hash
            }
            
            st.success("Secret locked!")
        else:
            st.error("Need both secret and password!")

          
elif page == "Open Secret":
    st.header("Open Secret Box")
    
    encrypted_input = st.text_area("Paste encrypted message:")
    password_guess = st.text_input("Enter password:", type="password")
    
    if st.button("Unlock"):
        if encrypted_input and password_guess:

            found = False
            for secret_id, secret_data in st.session_state.vault.items():
                
                if secret_data["password_hash"] == make_hash(password_guess):
                    
                    result = unlock_message(encrypted_input, password_guess)
                    if result:
                        st.success(f"Secret: {result}")
                        found = True
                        st.session_state.wrong_tries = 0
                        break
                        
            if not found:
                st.session_state.wrong_tries += 1
                st.error(f"Wrong! Tries left: {3 - st.session_state.wrong_tries}")
                
                if st.session_state.wrong_tries >= 3:
                    st.warning("System locked! Contact admin")
                    page = "Emergency Entry"
                    st.experimental_rerun()
        else:
            st.error("Need both fields!")


elif page == "Emergency Entry":
    st.header("ADMIN ACCESS ONLY")
    admin_pass = st.text_input("Master Key:", type="password")
    
    if st.button("Unlock System"):
        if admin_pass == "supersecret123":
            st.session_state.wrong_tries = 0
            st.success("System unlocked!")
            page = "Open Secret"
            st.experimental_rerun()
        else:
            st.error("Incorrect master key!")