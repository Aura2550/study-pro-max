import streamlit as st
import google.generativeai as genai

# --- UI CONFIG ---
st.set_page_config(page_title="STUDY-PRO ULTRA MAX", layout="wide")

# --- CSS (Glassmorphism) ---
st.markdown("""
    <style>
    .stApp { background: #020617; color: white; }
    .glass { background: rgba(255, 255, 255, 0.05); padding: 25px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.1); }
    .hero { font-size: 3.5rem; color: #22d3ee; text-align: center; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='hero'>STUDY-PRO ULTRA</h1>", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    api_key = st.text_input("ENTER API KEY:", type="password")
    mode = st.radio("SELECT FEATURE:", ["Research", "Slide Deck", "Exam Maker"])

# --- SMART MODEL LOADER (Fixes 404 Error) ---
def get_working_model(key):
    genai.configure(api_key=key)
    # List of models to try in order
    for model_name in ['gemini-pro', 'gemini-1.5-flash', 'gemini-1.5-pro']:
        try:
            m = genai.GenerativeModel(model_name)
            m.generate_content("test") # Test call
            return m
        except:
            continue
    return None

# --- MAIN LOGIC ---
if api_key:
    model = get_working_model(api_key)
    
    if model:
        topic = st.text_input("Enter your Topic (e.g. Newton's Laws):")
        if st.button("EXECUTE"):
            with st.spinner("AI is thinking..."):
                if mode == "Research":
                    prompt = f"Perform deep research on {topic} for Class 9. Detailed points."
                elif mode == "Slide Deck":
                    prompt = f"Create 10 slides outline for {topic}."
                else:
                    prompt = f"Create a Class 9 exam for {topic}."
                
                res = model.generate_content(prompt)
                st.markdown(f"<div class='glass'>{res.text}</div>", unsafe_allow_html=True)
    else:
        st.error("Model Error: Google is not accepting this key or model name. Please check your API key.")
else:
    st.warning("Sidebar mein API Key enter karein.")
