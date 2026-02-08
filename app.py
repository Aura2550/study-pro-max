import streamlit as st
import google.generativeai as genai
import pandas as pd

# --- ULTIMATE UI CONFIG ---
st.set_page_config(page_title="STUDY-PRO ULTRA MAX v4.0", layout="wide")

# --- ADVANCED CSS (Cyberpunk & Glassmorphism) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Inter:wght@300;500;700&display=swap');
    
    .stApp { background: radial-gradient(circle at top, #0f172a 0%, #020617 100%); color: #e2e8f0; font-family: 'Inter', sans-serif; }
    
    /* Neon Glow Header */
    .hero-text { font-family: 'Orbitron', sans-serif; font-size: 4rem; text-align: center; 
                 background: linear-gradient(to right, #22d3ee, #818cf8, #c084fc);
                 -webkit-background-clip: text; -webkit-text-fill-color: transparent;
                 filter: drop-shadow(0 0 15px rgba(34, 211, 238, 0.5)); margin-bottom: 5px; }
    
    /* Feature Cards */
    .glass-card { background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); 
                  padding: 30px; border-radius: 24px; backdrop-filter: blur(12px); 
                  box-shadow: 0 20px 40px rgba(0,0,0,0.4); transition: 0.5s; }
    .glass-card:hover { border: 1px solid #22d3ee; transform: translateY(-10px); box-shadow: 0 0 30px rgba(34, 211, 238, 0.2); }
    
    /* Inputs & Buttons */
    .stTextInput>div>div>input { background: #1e293b !important; color: white !important; border-radius: 12px !important; border: 1px solid #334155 !important; }
    .stButton>button { background: linear-gradient(45deg, #0891b2, #4f46e5); color: white; border: none; 
                        padding: 15px 30px; border-radius: 14px; font-weight: bold; width: 100%;
                        text-transform: uppercase; letter-spacing: 2px; transition: 0.4s; }
    .stButton>button:hover { box-shadow: 0 0 25px #0891b2; transform: scale(1.02); }
    
    /* Custom Sidebar */
    [data-testid="stSidebar"] { background-color: #030712 !important; border-right: 1px solid #1e293b; }
    </style>
    """, unsafe_allow_html=True)

# --- APP HEADER ---
st.markdown("<h1 class='hero-text'>STUDY-PRO ULTRA MAX</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 1.2rem;'>The Ultimate AI Powerhouse for Class 9 Toppers</p>", unsafe_allow_html=True)
st.markdown("---")

# --- SIDEBAR & SETUP ---
with st.sidebar:
    st.markdown("## 🛡️ CORE CONTROL")
    api_key = st.text_input("ENTER MASTER API KEY:", type="password", placeholder="Paste Gemini Key...")
    st.markdown("---")
    st.markdown("### 🛠️ SELECT ENGINE")
    mode = st.radio("", [
        "🌐 Deep Research (Perplexity Mode)", 
        "📑 Presentation Slide Deck", 
        "📝 Exam Master (Grand Test)",
        "📅 Weekly Study Planner",
        "📊 Performance Analyzer"
    ])
    st.markdown("---")
    st.info("System Engine: Gemini-1.5-Flash (Optimized)")

# --- MAIN LOGIC ---
if api_key:
    try:
        genai.configure(api_key=api_key)
        # Seed test to ensure it's working
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # 1. DEEP RESEARCH
        if mode == "🌐 Deep Research (Perplexity Mode)":
            st.markdown("### 🔍 World-Class Deep Research")
            topic = st.text_input("Enter your complex question or topic:")
            if st.button("EXECUTE DEEP DIVE"):
                with st.spinner("Analyzing Global Databases..."):
                    prompt = f"Act as a PhD researcher. Explain '{topic}' for a Class 9 student. Use clear headings: 1. Executive Summary 2. Deep Dive Analysis 3. Real World Application 4. Critical Facts."
                    res = model.generate_content(prompt)
                    st.markdown(f"<div class='glass-card'>{res.text}</div>", unsafe_allow_html=True)

        # 2. SLIDE DECK
        elif mode == "📑 Presentation Slide Deck":
            st.markdown("### 📽️ Professional Presentation Creator")
            s_topic = st.text_input("What is your presentation about?")
            if st.button("DESIGN SLIDE DECK"):
                with st.spinner("Drafting Slides..."):
                    prompt = f"Create a detailed 10-slide presentation outline on {s_topic} for Class 9. For each slide, provide a Title, 4 Bullet points, and a 'Visual Description' for AI Image generators."
                    res = model.generate_content(prompt)
                    st.markdown(f"<div class='glass-card'>{res.text}</div>", unsafe_allow_html=True)

        # 3. EXAM MASTER
        elif mode == "📝 Exam Master (Grand Test)":
            st.markdown("### ✍️ Ultimate Test Generator")
            subj = st.text_input("Subject/Chapter Name:")
            difficulty = st.select_slider("Select Difficulty", ["Easy", "Standard", "Legend"])
            if st.button("GENERATE GRAND TEST"):
                with st.spinner("Generating Paper..."):
                    prompt = f"Generate a {difficulty} level test for Class 9 {subj}. Include: 5 Advanced MCQs, 3 Conceptual Short Questions, 1 Long Question. Provide an Answer Key at the very bottom."
                    res = model.generate_content(prompt)
                    st.markdown(f"<div class='glass-card'>{res.text}</div>", unsafe_allow_html=True)

        # 4. STUDY PLANNER
        elif mode == "📅 Weekly Study Planner":
            st.markdown("### 🗓️ AI Time Management")
            goal = st.text_input("What is your goal? (e.g., Finish Physics in 1 week)")
            if st.button("CREATE PLAN"):
                prompt = f"Create a 7-day hour-by-hour study schedule for a Class 9 student to achieve this: {goal}. Make it realistic with breaks."
                res = model.generate_content(prompt)
                st.markdown(f"<div class='glass-card'>{res.text}</div>", unsafe_allow_html=True)

        # 5. PERFORMANCE ANALYZER
        elif mode == "📊 Performance Analyzer":
            st.markdown("### 📈 Grade Analysis")
            st.write("Enter your scores to see your level:")
            scores = st.slider("Your last test marks (%)", 0, 100, 50)
            if st.button("ANALYZE ME"):
                if scores >= 90:
                    st.success("LEVEL: LEGEND. You are in the top 1% of students.")
                elif scores >= 75:
                    st.info("LEVEL: PRO. You have strong basics, just need more practice.")
                else:
                    st.warning("LEVEL: LEARNER. Need to focus on Research and Exam Master mode.")

    except Exception as e:
        st.error(f"⚠️ Critical Error: {str(e)}")
        st.info("Tip: Make sure your API key is active and you have an internet connection.")

else:
    st.warning("🛑 MASTER KEY REQUIRED: Please enter your Gemini API Key in the sidebar to unlock Ultra features.")

st.markdown("<br><p style='text-align: center; color: #475569;'>Aura2550 | Study-Pro Ultra v4.0 Platinum Edition</p>", unsafe_allow_html=True)
