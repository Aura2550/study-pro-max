import streamlit as st
import google.generativeai as genai

# --- PAGE CONFIG ---
st.set_page_config(page_title="STUDY-PRO ULTRA MAX", layout="wide", initial_sidebar_state="expanded")

# --- UI DESIGN (CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&family=Inter:wght@400;600&display=swap');
    .stApp { background: radial-gradient(circle, #0f172a 0%, #020617 100%); color: #f8fafc; font-family: 'Inter', sans-serif; }
    .main-title { font-family: 'Orbitron', sans-serif; font-size: 3rem; text-align: center; 
                  background: linear-gradient(90deg, #22d3ee, #818cf8, #c084fc);
                  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
                  filter: drop-shadow(0 0 15px rgba(34, 211, 238, 0.4)); margin-bottom: 30px; }
    .stButton>button { background: linear-gradient(45deg, #06b6d4, #6366f1); color: white; border: none; 
                        padding: 12px; border-radius: 12px; font-weight: bold; transition: 0.3s; width: 100%; }
    .stButton>button:hover { transform: translateY(-2px); box-shadow: 0 0 20px rgba(99, 102, 241, 0.6); }
    .result-card { background: rgba(30, 41, 59, 0.7); border: 1px solid rgba(255, 255, 255, 0.1); 
                   padding: 25px; border-radius: 20px; backdrop-filter: blur(10px); margin-top: 20px; line-height: 1.6; }
    .stTextInput>div>div>input { background: #1e293b !important; color: white !important; border-radius: 10px !important; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown("<h1 class='main-title'>STUDY-PRO ULTRA MAX</h1>", unsafe_allow_html=True)

# --- SIDEBAR (SETUP & NAVIGATION) ---
with st.sidebar:
    st.markdown("### 🔑 ACCESS CONTROL")
    user_api_key = st.text_input("Master API Key:", type="password", placeholder="Enter Gemini Key...")
    st.markdown("---")
    st.markdown("### 🚀 NAVIGATION")
    mode = st.radio("Select Tool:", [
        "🌐 Perplexity Deep Research", 
        "📑 Professional Slide Deck", 
        "📝 Ultimate Exam Maker",
        "📊 Performance AI"
    ])
    st.markdown("---")
    st.caption("Status: System Active v3.5")

# --- MODEL INITIALIZER (AUTO-FIX BUGS) ---
def get_model(api_key):
    genai.configure(api_key=api_key)
    # List of models to try in order of performance
    models_to_try = ['gemini-1.5-flash-latest', 'gemini-1.5-flash', 'gemini-pro']
    
    for m_name in models_to_try:
        try:
            model = genai.GenerativeModel(m_name)
            # Test simple call
            model.generate_content("test")
            return model
        except:
            continue
    return None

# --- MAIN LOGIC ---
if user_api_key:
    active_model = get_model(user_api_key)
    
    if active_model:
        # 1. DEEP RESEARCH
        if mode == "🌐 Perplexity Deep Research":
            st.subheader("🔍 AI Research Engine")
            topic = st.text_input("Enter topic for deep analysis:")
            if st.button("START RESEARCH"):
                with st.spinner("Analyzing world data..."):
                    prompt = f"Perform deep research on {topic} for Class 9. Provide a Summary, 5 Detailed Points, and 3 Interesting Facts."
                    response = active_model.generate_content(prompt)
                    st.markdown(f"<div class='result-card'>{response.text}</div>", unsafe_allow_html=True)

        # 2. SLIDE DECK
        elif mode == "📑 Professional Slide Deck":
            st.subheader("🖼️ Slide Content Generator")
            s_topic = st.text_input("Topic for slides:")
            if st.button("DESIGN DECK"):
                with st.spinner("Generating outline..."):
                    prompt = f"Create a 10-slide presentation outline for {s_topic} (Class 9). Include Title, Bullet points, and visual ideas for each slide."
                    response = active_model.generate_content(prompt)
                    st.markdown(f"<div class='result-card'>{response.text}</div>", unsafe_allow_html=True)

        # 3. EXAM MAKER
        elif mode == "📝 Ultimate Exam
