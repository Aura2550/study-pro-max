import streamlit as st
import google.generativeai as genai

# --- ULTRA MODERN UI CONFIG ---
st.set_page_config(page_title="STUDY-PRO ULTRA", layout="wide", initial_sidebar_state="collapsed")

# --- CSS FOR HIGH-END INTERFACE ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&family=Orbitron:wght@700&display=swap');
    .stApp { background: #0a0b10; color: #ffffff; font-family: 'Poppins', sans-serif; }
    .main-title { font-family: 'Orbitron', sans-serif; font-size: 3.5rem; text-align: center; 
                  background: linear-gradient(90deg, #00f2fe, #4facfe, #7000ff);
                  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
                  margin-bottom: 0px; filter: drop-shadow(0 0 10px #00f2fe); }
    .card { background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(0, 242, 254, 0.2);
             padding: 25px; border-radius: 20px; backdrop-filter: blur(10px); 
             box-shadow: 0 10px 30px rgba(0,0,0,0.5); transition: 0.4s; margin-bottom: 20px; }
    .stButton>button { width: 100%; background: linear-gradient(45deg, #00f2fe, #7000ff); 
                        border: none; color: white; font-weight: 600; padding: 15px;
                        border-radius: 12px; transition: 0.3s; }
    [data-testid="stSidebar"] { background-color: #0f1116 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- APP LAYOUT ---
st.markdown("<h1 class='main-title'>STUDY-PRO ULTRA</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888;'>The World's Most Powerful Class 9 AI Tutor</p>", unsafe_allow_html=True)

# Sidebar for Setup
with st.sidebar:
    st.markdown("### ⚙️ SETTINGS")
    api_key = st.text_input("Master API Key:", type="password", placeholder="Enter your key...")
    st.markdown("---")
    mode = st.selectbox("CHOOSE FEATURE", 
                        ["🌐 Perplexity Research", "📑 Slide Deck Pro", "📝 Grand Test Maker", "🎙️ Voice Tutor"])
    st.info("System Status: Online")

# --- CORE LOGIC ---
if api_key:
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')

        # 1. DEEP RESEARCH
        if mode == "🌐 Perplexity Research":
            topic = st.text_input("What do you want to master today?")
            if st.button("EXECUTE RESEARCH"):
                with st.spinner("Analyzing..."):
                    res = model.generate_content(f"Deep research on '{topic}' for Class 9. Detailed and clear.")
                    st.markdown(f"<div class='card'>{res.text}</div>", unsafe_allow_html=True)

        # 2. SLIDE DECK PRO
        elif mode == "📑 Slide Deck Pro":
            topic = st.text_input("Topic for Presentation:")
            if st.button("GENERATE SLIDES"):
                with st.spinner("Designing..."):
                    res = model.generate_content(f"Create a 7-slide outline for {topic}. Class 9 level.")
                    st.markdown(f"<div class='card'>{res.text}</div>", unsafe_allow_html=True)

        # 3. GRAND TEST MAKER
        elif mode == "📝 Grand Test Maker":
            subj = st.text_input("Enter Subject/Chapter:")
            if st.button("CREATE EXAM"):
                res = model.generate_content(f"Create a Class 9 exam for {subj} with MCQs and Answers.")
                st.markdown(f"<div class='card'>{res.text}</div>", unsafe_allow_html=True)

        # 4. VOICE TUTOR
        elif mode == "🎙️ Voice Tutor":
            txt = st.text_area("Paste text to read aloud:")
            if st.button("SPEAK"):
                st.markdown(f"<script>var msg = new SpeechSynthesisUtterance('{txt}'); window.speechSynthesis.speak(msg);</script>", unsafe_allow_html=True)
                st.success("Tutor is speaking...")

    except Exception as e:
        st.error(f"Something went wrong: {e}")
else:
    st.warning("⚠️ Sidebar mein API Key daalein.")
