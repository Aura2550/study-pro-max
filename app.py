import streamlit as st
import google.generativeai as genai

# --- PAGE CONFIG ---
st.set_page_config(page_title="STUDY-PRO ULTRA", layout="wide")

# --- UI DESIGN (CSS) ---
st.markdown("""
    <style>
    .stApp { background: #020617; color: #f8fafc; }
    .main-title { font-size: 3rem; text-align: center; color: #22d3ee; font-weight: bold; margin-bottom: 20px; }
    .card { background: #1e293b; border: 1px solid #334155; padding: 20px; border-radius: 15px; margin-top: 20px; }
    .stButton>button { background: linear-gradient(90deg, #06b6d4, #6366f1); color: white; border-radius: 10px; border: none; padding: 10px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>STUDY-PRO ULTRA MAX</h1>", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.header("SETUP")
    api_key = st.text_input("Gemini API Key:", type="password")
    st.markdown("---")
    mode = st.radio("SELECT TOOL:", ["Research", "Slide Deck", "Exam Maker"])

# --- AUTO-MODEL FINDER ---
def load_ai(key):
    genai.configure(api_key=key)
    for m in ['gemini-1.5-flash', 'gemini-pro']:
        try:
            model = genai.GenerativeModel(m)
            model.generate_content("test")
            return model
        except:
            continue
    return None

# --- MAIN LOGIC ---
if api_key:
    ai = load_ai(api_key)
    if ai:
        # 1. RESEARCH
        if mode == "Research":
            topic = st.text_input("Enter Topic for Research:")
            if st.button("RUN RESEARCH"):
                res = ai.generate_content(f"Deep research on {topic} for Class 9 student.")
                st.markdown(f"<div class='card'>{res.text}</div>", unsafe_allow_html=True)

        # 2. SLIDE DECK
        elif mode == "Slide Deck":
            topic = st.text_input("Topic for Presentation:")
            if st.button("MAKE SLIDES"):
                res = ai.generate_content(f"Create a 10-slide outline for {topic}.")
                st.markdown(f"<div class='card'>{res.text}</div>", unsafe_allow_html=True)

        # 3. EXAM MAKER
        elif mode == "Exam Maker":
            topic = st.text_input("Subject/Chapter:")
            if st.button("START TEST"):
                res = ai.generate_content(f"Create a Class 9 test for {topic} with answers.")
                st.markdown(f"<div class='card'>{res.text}</div>", unsafe_allow_html=True)
    else:
        st.error("API Key is valid but models are busy. Try again in 1 minute.")
else:
    st.warning("Please enter your API Key in the sidebar.")
