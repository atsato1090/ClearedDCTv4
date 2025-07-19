import streamlit as st
from streamlit_lottie import st_lottie
import requests

st.set_page_config(page_title="ClearedDCT - Welcome", page_icon="✈️", layout="centered")

# Load Lottie animation
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

clouds_animation = load_lottie_url("https://lottie.host/fb06d1a7-f046-40d0-ae15-1990a4ad8ebf/mZ1B7GVQZ0.json")

# Background color and styling
st.markdown(
    """
    <style>
    body, .stApp {
        background-color: #e6f2ff;
        color: #003366;
    }
    .stButton>button {
        background-color: #0066cc;
        color: white;
        font-size: 20px;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 24px;
    }
    .stButton>button:hover {
        background-color: #004c99;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display animation and logo
st_lottie(clouds_animation, speed=1, height=300, key="clouds")
st.image("logo_loading.png", use_column_width=True, caption="ClearedDCT - ATC Flight Plan App")

st.write("## Welcome to ClearedDCT")
st.write("Your intuitive ICAO flight plan and messaging tool for student ATCs and instructors.")

# Enter button logic
if st.button("Enter App ✈️"):
    js = "window.open('https://YOUR_CLEAREDDCT_APP_URL_HERE','_self')"
    html = f'<img src onerror="{js}">'
    st.components.v1.html(html)

