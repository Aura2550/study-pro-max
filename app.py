import streamlit as st
import google.generativeai as genai
import os

# --- ULTIMATE UI ---
st.set_page_config(page_title="STUDY-PRO BEYOND v8.0", layout="wide")
st.markdown("""<style>
    .stApp { background: #010409; color: white; }
    .card { background: #161b22; border: 1px solid #30363d; padding: 20px; border-radius: 10px; }
    .title { color: #58a6ff; font-weight: bold; font-size: 3rem; text-align: center; }
</style>""", unsafe_allow_html=True)

st.markdown("<h1 class='title'>STUDY-PRO BEYOND</h1>", unsafe_allow_html=True)

with st.sidebar:
    api_key = st.text_input("ENTER MASTER KEY:", type="password")
    mode = st.selectbox("MODULE", ["Research", "Exam", "Slides"])

# --- THE BYPASS LOGIC ---
if api_key:
    try:
        # Step 1: Clear any old configuration
        genai.configure(api_key=api_key)
        
        # Step 2: Try models with full naming convention
        # We use 'gemini-1.5-flash-8b' also, as it's often more available
        working_model = None
        for m_name in ['gemini-1.5-flash', 'gemini-1.5-flash-8b', 'gemini-pro']:
            try:
                m = genai.GenerativeModel(m_name)
                # Force a tiny test response
                test_check = m.generate_content("hi")
                if test_check:
                    working_model = m
                    break
            except:
                continue

        if working_model:
            st.success("⚡ NEURAL LINK ESTABLISHED!")
            topic = st.text_input("Enter Topic:")
            if st.button("EXECUTE"):
                res = working_model.generate_content(f"Explain {topic} for Class 9.")
                st.markdown(f"<div class='card'>{res.text}</div>", unsafe_allow_html=True)
        else:
            # AGAR YAHAN BHI FAIL HUA, TO MASLA CODE MEIN NAHI HAI
            st.error("🚨 GOOGLE ACCOUNT RESTRICTION: Aapka account ya region is model ko allow nahi kar raha.")
            st.info("Solution: 1. Google AI Studio mein ja kar ek baar 'Chat' mein kuch likhen. 2. Agar wahan 'Safety Warning' aaye toh use accept karein.")
            
    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.warning("Please enter API Key.")
