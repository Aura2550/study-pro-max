import streamlit as st
import google.generativeai as genai

# --- 1. ULTIMATE CONFIG ---
st.set_page_config(page_title="STUDY-PRO BEYOND v7.0", layout="wide")

# --- 2. ELITE CYBERPUNK CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Rajdhani:wght@300;500;700&display=swap');
    
    .stApp { background: #050505; color: #e0e0e0; font-family: 'Rajdhani', sans-serif; }
    
    /* Neon Header */
    .title-container { text-align: center; padding: 20px; border-bottom: 2px solid #00f2fe; margin-bottom: 30px; background: rgba(0,242,254,0.05); }
    .main-title { font-family: 'Orbitron', sans-serif; font-size: 4rem; font-weight: 900; 
                  background: linear-gradient(90deg, #00f2fe, #7000ff, #00f2fe);
                  background-size: 200% auto; -webkit-background-clip: text; -webkit-text-fill-color: transparent;
                  animation: shine 3s linear infinite; }
    @keyframes shine { to { background-position: 200% center; } }

    /* Futuristic Cards */
    .feature-card { background: rgba(15, 15, 15, 0.95); border-left: 5px solid #00f2fe;
                    padding: 30px; border-radius: 0 20px 20px 0; margin-bottom: 25px;
                    box-shadow: 10px 10px 30px rgba(0,0,0,0.5); border-top: 1px solid #333; }
    
    /* Neon Input & Buttons */
    .stTextInput>div>div>input { background: #111 !important; color: #00f2fe !important; border: 1px solid #00f2fe !important; font-size: 1.2rem !important; }
    .stButton>button { background: linear-gradient(45deg, #00f2fe, #7000ff); color: white; border: none;
                        padding: 15px 40px; border-radius: 5px; font-family: 'Orbitron'; font-weight: bold;
                        text-transform: uppercase; letter-spacing: 3px; transition: 0.5s; width: 100%; }
    .stButton>button:hover { box-shadow: 0 0 30px #00f2fe; transform: scale(1.02); }

    [data-testid="stSidebar"] { background-color: #000 !important; border-right: 1px dotted #00f2fe; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. CORE SYSTEM INTERFACE ---
st.markdown("<div class='title-container'><h1 class='main-title'>STUDY-PRO BEYOND</h1><p style='letter-spacing:5px; color:#7000ff;'>V7.0 PLATINUM EDITION</p></div>", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("<h2 style='color:#00f2fe; font-family:Orbitron;'>⚡ CORE ACCESS</h2>", unsafe_allow_html=True)
    api_key = st.text_input("ENTER MASTER KEY:", type="password")
    st.markdown("---")
    mode = st.selectbox("COMMAND CENTER", ["🌐 Deep Research", "📑 Slide Architect", "📝 Exam Master", "📅 Study Strat", "🎙️ AI Tutor"])
    st.success("System Status: Ready")

# --- 4. ENGINE LOGIC (FIXED BRACKETS & FALLBACKS) ---
if api_key:
    try:
        genai.configure(api_key=api_key)
        
        # Self-healing model selection
        def connect_brain():
            models = ['gemini-1.5-flash', 'gemini-1.5-flash-latest', 'gemini-pro']
            for m in models:
                try:
                    engine = genai.GenerativeModel(m)
                    engine.generate_content("ping")
                    return engine
                except: continue
            return None

        brain = connect_brain()

        if brain:
            st.markdown("<div class='feature-card'>", unsafe_allow_html=True)
            topic = st.text_input("WHAT IS YOUR OBJECTIVE?")
            execute = st.button("INITIALIZE MISSION")
            st.markdown("</div>", unsafe_allow_html=True)

            if execute and topic:
                with st.spinner("Decoding Neural Data..."):
                    if mode == "🌐 Deep Research":
                        prompt = f"Advanced PhD level research on {topic} for Class 9. Explain like a genius."
                    elif mode == "📑 Slide Architect":
                        prompt = f"10 detailed slides for {topic} presentation with visual cues."
                    elif mode == "📝 Exam Master":
                        prompt = f"Grand Test for Class 9 {topic} with Answers."
                    elif mode == "📅 Study Strat":
                        prompt = f"Detailed 7-day master plan for {topic}."
                    else:
                        prompt = f"Act as a voice tutor. Explain {topic} simply."
                    
                    response = brain.generate_content(prompt)
                    st.markdown("### 📡 NEURAL OUTPUT")
                    st.markdown(f"<div class='feature-card' style='border-left-color:#7000ff;'>{response.text}</div>", unsafe_allow_html=True)
        else:
            st.error("Model Error: Your API key is valid but Google is blocking the connection. Try a different Key.")

    except Exception as e:
        st.error(f"Critical System Failure: {str(e)}")
else:
    st.warning("⚠️ ACCESS DENIED: PLEASE INSERT MASTER KEY IN SIDEBAR")

st.markdown("<p style='text-align: center; color: #444;'>// AURA-2550 // NEURAL LINK STABLE</p>", unsafe_allow_html=True)
