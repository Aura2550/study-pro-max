import streamlit as st
import google.generativeai as genai

# --- 1. CONFIG & UI (Wahi purana khoobsurat look) ---
st.set_page_config(page_title="STUDY-PRO BEYOND v7.0", layout="wide")
st.markdown("""
    <style>
    .stApp { background: #050505; color: #e0e0e0; font-family: 'Rajdhani', sans-serif; }
    .main-title { font-size: 3.5rem; text-align: center; background: linear-gradient(90deg, #00f2fe, #7000ff); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: bold; }
    .feature-card { background: rgba(15, 15, 15, 0.95); border-left: 5px solid #00f2fe; padding: 25px; border-radius: 10px; margin-top: 20px; }
    .stButton>button { background: linear-gradient(45deg, #00f2fe, #7000ff); color: white; border: none; padding: 12px; border-radius: 5px; width: 100%; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>STUDY-PRO BEYOND</h1>", unsafe_allow_html=True)

# --- 2. SIDEBAR ---
with st.sidebar:
    st.header("⚡ CORE ACCESS")
    api_key = st.text_input("ENTER MASTER KEY:", type="password")
    mode = st.selectbox("COMMAND CENTER", ["🌐 Deep Research", "📑 Slide Architect", "📝 Exam Master"])

# --- 3. THE ULTIMATE FIX (Blocking Bypass) ---
if api_key:
    try:
        # Force connection using the most stable method
        genai.configure(api_key=api_key)
        
        # HUM ALAG ALAG MODELS AUR PATHS TRY KARENGE
        def connect_to_brain():
            # 1. Sabse pehle poora path try karein (Google isse block nahi karta)
            # 2. Phir normal flash try karein
            # 3. Phir pro try karein
            model_names = ['models/gemini-1.5-flash', 'gemini-1.5-flash', 'gemini-pro']
            
            for name in model_names:
                try:
                    m = genai.GenerativeModel(model_name=name)
                    # Chota sa test call check karne ke liye ke block toh nahi
                    m.generate_content("test", generation_config={"max_output_tokens": 10})
                    return m, name
                except:
                    continue
            return None, None

        brain, active_name = connect_to_brain()

        if brain:
            st.success(f"🚀 SYSTEM ONLINE: Connected via {active_name}")
            topic = st.text_input("WHAT IS YOUR OBJECTIVE?")
            if st.button("INITIALIZE MISSION"):
                with st.spinner("Decoding Neural Data..."):
                    res = brain.generate_content(f"Explain {topic} for Class 9 in detail.")
                    st.markdown(f"<div class='feature-card'>{res.text}</div>", unsafe_allow_html=True)
        else:
            # AGAR SAB FAIL HO JAYE TO YE MESSAGE DIKHAO
            st.error("❌ GOOGLE BLOCK: API key sahi hai par Google models access nahi karne de raha. Solution: Google AI Studio mein ja kar 'Terms of Service' accept karein ya nayi key banayein.")
            
    except Exception as e:
        st.error(f"Critical System Failure: {str(e)}")
else:
    st.warning("⚠️ ACCESS DENIED: PLEASE INSERT MASTER KEY")
