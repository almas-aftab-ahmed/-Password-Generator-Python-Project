import streamlit as st
import random
import string
import re
import html

# Custom Styling
st.markdown("""
    <style>
        body {background: linear-gradient(to right, #ff9a9e, #fad0c4); font-family: Arial, sans-serif;}
        .title {color: #ff1493; text-align: center; font-size: 50px; font-weight: bold; text-shadow: 2px 2px 10px #ff69b4;}
        .stButton>button {background-color: #ff69b4; color: white; font-size: 20px; border-radius: 12px; padding: 10px; box-shadow: 2px 2px 10px #ff1493; transition: 0.3s;}
        .stButton>button:hover {background-color: #ff1493; transform: scale(1.1);}
        .result-box {text-align: center; font-size: 30px; font-weight: bold; color: #c71585; background: #fff; padding: 10px; border-radius: 10px; box-shadow: 2px 2px 10px #ff69b4; margin-top: 20px;}
        .copy-button {background-color: #ff69b4; color: white; font-size: 18px; border-radius: 10px; padding: 8px; cursor: pointer; transition: 0.3s; width: 200px; text-align: center; display: block; margin: 10px auto;}
        .copy-button:hover {background-color: #ff1493;}
        .strength-box {text-align: center; font-size: 22px; font-weight: bold; padding: 10px; border-radius: 10px; margin-top: 20px;}
        .weak {background-color: #ff4d4d; color: white;}
        .medium {background-color: #ffcc00; color: black;}
        .strong {background-color: #4caf50; color: white;}
        .footer {text-align: center; font-size: 18px; font-weight: bold; color: #ff1493; margin-top: 50px;}
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='title'>🔐 Password Generator and Strength Manager 💕</h1>", unsafe_allow_html=True)

# User Inputs
length = st.slider("Select Password Length:", 6, 30, 12)
use_upper = st.checkbox("Include Uppercase Letters (A-Z)")
use_lower = st.checkbox("Include Lowercase Letters (a-z)", value=True)
use_numbers = st.checkbox("Include Numbers (0-9)")
use_symbols = st.checkbox("Include Symbols (!@#$%^&*)")

# Generate Password
def generate_password():
    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        # Special characters excluding problematic HTML ones
        safe_symbols = "!@#$%^&*()_+=-{}[]"
        characters += safe_symbols
    
    if not characters:
        return "Please select at least one option!"
    
    return "".join(random.choice(characters) for _ in range(length))

# Password Strength Checker
def check_strength(password):
    if len(password) < 8:
        return "Weak", "weak"
    elif re.search(r"[A-Z]", password) and re.search(r"\d", password) and re.search(r"\W", password):
        return "Strong", "strong"
    else:
        return "Medium", "medium"

password = ""
if st.button("Generate Password 💖"):
    password = generate_password()

if password:
    if password == "Please select at least one option!":
        st.warning(password)
    else:
        # Escape the password for safe display
        escaped_password = html.escape(password)
        
        st.markdown(f"<h2 class='result-box'>{escaped_password}</h2>", unsafe_allow_html=True)

        # Strength Meter
        strength, strength_class = check_strength(password)
        st.markdown(f"<div class='strength-box {strength_class}'>Password Strength: {strength}</div>", unsafe_allow_html=True)

        # Copy Button with Hidden Input Field
        st.text_input("Generated Password", password, key="password", type="default")
        st.button("📋 Copy Password")

# Footer
st.markdown("<p class='footer'>✨ Made with ❤️ by Almas ✨</p>", unsafe_allow_html=True)
