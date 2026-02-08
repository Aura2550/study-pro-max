import streamlit as st
import google.generativeai as genai

# UI Setup
st.set_page_config(page_title="STUDY-PRO ULTRA", layout="wide")
st.markdown("<h1 style='text-align:center; color:#58a6ff;'>🎓 STUDY-PRO ULTRA MAX</h1>", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("Settings")
    new_key = st.text_input("Paste Fresh API Key:", type="password")
    mode = st.selectbox("Select Mode:", ["Research", "Exam Maker", "Slide Deck"])

# Logic
if new_key:
    try:
        genai.configure(api_key=new_key)
        # Using the most stable model name
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        topic = st.text_input("Enter Topic:")
        if st.button("Generate"):
            with st.spinner("Processing..."):
                prompt = f"Explain {topic} for Class 9 in detail with headings."
                if mode == "Exam Maker":
                    prompt = f"Create a Class 9 test for {topic} with answers."
                elif mode == "Slide Deck":
                    prompt = f"Create a 7-slide outline for {topic}."
                
                response = model.generate_content(prompt)
                st.info("Neural Output:")
                st.markdown(response.text)
                
    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.warning("Please enter the NEW API key in the sidebar.")
