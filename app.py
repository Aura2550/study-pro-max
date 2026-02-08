import streamlit as st
import requests
import json
import pandas as pd

# --- 1. ULTRA HIGH-END CONFIG ---
st.set_page_config(page_title="STUDY-PRO BEYOND v10.0", layout="wide")

# --- 2. EXTREME CSS (Cyberpunk Platinum Edition) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Inter:wght@300;600&family=JetBrains+Mono&display=swap');
    
    .stApp { background: radial-gradient(circle at top right, #0a0e14, #010409); color: #e6edf3; font-family: 'Inter', sans-serif; }
    
    /* Neon Glow Title */
    .hero-title { font-family: 'Orbitron', sans-serif; font-size: 4.5rem; text-align: center; font-weight: 900;
                  background: linear-gradient(90deg, #00f2fe, #7000ff, #00f2fe);
                  background-size: 200% auto; -webkit-background-clip: text; -webkit-text-fill-color: transparent;
                  animation: shine 4s linear infinite; filter: drop-shadow(0 0 15px rgba(0,242,254,0.4)); }
    @keyframes shine { to { background-position: 200% center; } }

    /* Glassmorphism Cards */
    .feature-card { background: rgba(22, 27, 34, 0.7); border: 1px solid rgba(88, 166, 255, 0.2);
                    padding: 30px; border-radius: 25px; backdrop-filter: blur(20px);
                    box-shadow: 0 15px 35px rgba(0,0,0,0.6); margin-top: 25px; transition: 0.4s; }
    .feature-card:hover { border: 1px solid #00f2fe; transform: translateY(-10px); box-shadow: 0 0 30px rgba(0,242,254,0.2); }

    /* Custom Buttons & Inputs */
    .stButton>button { background: linear-gradient(45deg, #00f2fe, #7000ff); color: white; border: none;
                        padding: 18px; border-radius: 12px; font-family: 'Orbitron'; font-weight: bold;
                        text-transform: uppercase; letter-spacing: 4px; transition: 0.5s; width: 100%; }
    .stButton>button:hover { box-shadow: 0 0 40px #00f2fe; letter-spacing: 6px; }
    
    .stTextInput>div>div>input { background: #0d1117 !important; color: #00f2fe !important; border: 1px solid #30363d !important; border-radius: 10px !important; }
    
    [data-testid="stSidebar"] { background-color: #000 !important; border-right: 2px solid #7000ff; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. THE INTERFACE ---
st.markdown("<h1 class='hero-title'>STUDY-PRO BEYOND</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; letter-spacing: 8px; color: #8b949e;'>V10.0 // NEURAL LINK TERMINAL</p>", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("<h2 style='color:#00f2fe; font-family:Orbitron;'>🔐 ACCESS</h2>", unsafe_allow_html=True)
    api_key = st.text_input("MASTER API KEY:", type="password", placeholder="Neural Key Required...")
    st.markdown("---")
    st.markdown("### 🚀 MODULES")
    mode = st.radio("", ["🌐 Deep Intelligence", "📝 Exam Architect", "📊 Performance AI", "📑 Presentation Deck", "🕒 Study Planner"])
    st.success("SYSTEM READY")

# --- 4. THE POWERFUL DIRECT ENGINE ---
def call_neural_engine(key, prompt):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={key}"
    headers = {'Content-Type': 'application/json'}
    data = {"contents": [{"parts": [{"text": prompt}]}]}
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data), timeout=15)
        res_json = response.json()
        if 'candidates' in res_json:
            return res_json['candidates'][0]['content']['parts'][0]['text']
        return f"ERROR: {res_json.get('error', {}).get('message', 'Key Invalid or Expired')}"
    except:
        return "CONNECTION FAILURE: Check Internet."

# --- 5. MAIN WORKSPACE ---
if api_key:
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("<div class='feature-card'>", unsafe_allow_html=True)
        st.markdown("### 🎯 INPUT OBJECTIVE")
        topic = st.text_input("Enter Topic for Analysis:")
        execute = st.button("INITIALIZE MISSION")
        st.markdown("</div>", unsafe_allow_html=True)
        
    if execute and topic:
        with st.spinner("Decoding Knowledge..."):
            # Intelligent Prompts
            if mode == "🌐 Deep Intelligence":
                p = f"Deep Research on {topic} for Class 9. Detailed sections, facts, and analogies."
            elif mode == "📝 Exam Architect":
                p = f"Create a Class 9 Exam for {topic}. 5 MCQs, 3 Short Qs, 1 Logical Q. Include Answers."
            elif mode == "📑 Presentation Deck":
                p = f"10 Slide Deck for {topic} for Class 9. Title and content for each slide."
            elif mode == "🕒 Study Planner":
                p = f"7-day master study plan for {topic} for a student."
            else:
                p = f"Explain {topic} in depth for a student."

            output = call_neural_engine(api_key, p)
            
            with col2:
                st.markdown("<div class='feature-card'>", unsafe_allow_html=True)
                st.markdown("### 🧬 OUTPUT DATA")
                st.markdown(output)
                
                # Dynamic Diagram Trigger
                if any(word in topic.lower() for word in ["heart", "atom", "cell", "cycle"]):
                     st.info("💡 Pro Tip: Study the diagram below for better visualization.")
                     if "heart" in topic.lower(): st.markdown("

[Image of the human heart anatomy]
")
                     elif "atom" in topic.lower(): st.markdown("

[Image of Bohr's atomic model]
")
                     elif "cell" in topic.lower(): st.markdown("

[Image of animal cell vs plant cell]
")
                
                st.markdown("</div>", unsafe_allow_html=True)
else:
    st.warning("📡 WAITING FOR MASTER KEY... ACCESS DENIED")

st.markdown("<br><hr><p style='text-align: center; color: #30363d;'>// AURA-2550 // 2026 // NO BOUNDARIES</p>", unsafe_allow_html=True)
