import streamlit as st
import google.generativeai as genai

# Page Configuration
st.set_page_config(page_title="STUDY-PRO MAX", layout="wide")

# Sidebar for API Key
with st.sidebar:
    st.title("🛠️ Setup")
    api_key = st.text_input("Enter Gemini API Key:", type="password")
    if api_key:
        st.success("API Key Saved!")

# Main App Logic
st.title("🎓 STUDY-PRO MAX: Class 9")

if api_key:
    genai.configure(api_key=api_key)
    menu = st.sidebar.radio("Navigation", ["Research Engine", "Quiz Maker"])
    
    if menu == "Research Engine":
        st.header("🔍 AI Research Engine")
        topic = st.text_input("Apna Topic likhen (e.g., Photosynthesis):")
        if st.button("Search"):
            model = genai.GenerativeModel('gemini-1.5-flash')
            res = model.generate_content(topic)
            st.markdown(res.text)
else:
    st.warning("Please enter your Gemini API Key in the sidebar to start.")
