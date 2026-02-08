import streamlit as st
import google.generativeai as genai

# --- 1. POWER UI CONFIG ---
st.set_page_config(page_title="STUDY-PRO PLATINUM", layout="wide")

# --- 2. ELITE CSS (NotebookLM + Perplexity Look) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Orbitron:wght@600&display=swap');
    .stApp { background: #0d1117; color: #c9d1d9; font-family: 'Inter', sans-serif; }
    .header { font-family: 'Orbitron', sans-serif; font-size: 3rem; text-align: center; color: #58a6ff; margin-bottom: 0; }
    .subtitle { text-align: center; color: #8b949e; margin-bottom: 40px; }
    .card { background: #161b22; border: 1px solid #30363d; padding: 25px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); }
    .stButton>button { background: #238636; color: white; border: none; padding: 12px; border-radius: 6px; width: 100%; font-weight: bold; cursor: pointer; }
    .stButton>button:hover { background: #2ea043; }
    .stTextInput>div>div>input { background: #0d1117 !important; color: white !important; border: 1px solid #30363d !important; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='header'>STUDY-PRO BEYOND</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>V7.0 PLATINUM | AI-POWERED CLASS 9 TUTOR</p>", unsafe_allow_html=True)

# --- 3. SIDEBAR & KEY ---
with st.sidebar:
    st.markdown("### 🔑 SYSTEM ACCESS")
    key = st.text_input("ENTER NEW API KEY:", type="password")
    st.markdown("---")
    mode = st.radio("SELECT ENGINE:", ["🌐 Deep Research", "📝 Exam Architect", "📑 Presentation Deck", "💡 Concept Explainer"])
    st.info("Status: Ready for Neural Link")

# --- 4. THE UNSTOPPABLE LOGIC ---
if key:
    try:
        genai.configure(api_key=key)
        
        # Try finding a working model
        def load_brain():
            for m_name in ['gemini-1.5-flash', 'gemini-pro', 'gemini-1.5-pro']:
                try:
                    m = genai.GenerativeModel(m_name)
                    m.generate_content("hi")
                    return m
                except: continue
            return None

        model = load_brain()

        if model:
            st.success("✅ CONNECTION ESTABLISHED")
            
            with st.container():
                st.markdown("<div class='card'>", unsafe_allow_html=True)
                topic = st.text_input("What would you like to master today?")
                btn = st.button("RUN AI ENGINE")
                st.markdown("</div>", unsafe_allow_html=True)

            if btn and topic:
                with st.spinner("Analyzing Knowledge..."):
                    # Custom Prompts based on Mode
                    prompts = {
                        "🌐 Deep Research": f"Research '{topic}' for Class 9. Give a summary, detailed analysis, and key facts.",
                        "📝 Exam Architect": f"Create a Class 9 exam for '{topic}' with 5 MCQs and 2 Long Questions. Include answers.",
                        "📑 Presentation Deck": f"Create a 10-slide outline for '{topic}' with titles and visual ideas.",
                        "💡 Concept Explainer": f"Explain '{topic}' like I'm 14. Use simple analogies and examples."
                    }
                    
                    response = model.generate_content(prompts[mode])
                    st.markdown("### 🧬 Neural Output")
                    st.markdown(f"<div class='card' style='line-height:1.8;'>{response.text}</div>", unsafe_allow_html=True)
        else:
            st.error("🚨 GOOGLE ERROR: API Key detect ho rahi hai par access block hai. AI Studio mein 'Chat' karke key refresh karein.")

    except Exception as e:
        st.error(f"System Failure: {e}")
else:
    st.warning("⚠️ Waiting for Master Key in Sidebar...")

st.markdown("<br><p style='text-align: center; color: #484f58;'>Aura2550 // 2026 Neural Link</p>", unsafe_allow_html=True)
