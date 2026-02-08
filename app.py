import streamlit as st
import google.generativeai as genai
import time

# --- ADVANCED UI/CSS ---
st.set_page_config(page_title="STUDY-PRO ULTRA MAX", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Inter:wght@300;500&display=swap');
    
    .stApp { background: #05070a; color: #e0e0e0; font-family: 'Inter', sans-serif; }
    .stButton>button { 
        background: linear-gradient(45deg, #00f2fe 0%, #4facfe 100%); 
        color: black; font-weight: bold; border: none; border-radius: 12px;
        transition: 0.3s; box-shadow: 0px 4px 15px rgba(79, 172, 254, 0.4);
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0px 6px 20px rgba(0, 242, 254, 0.6); }
    .sidebar .sidebar-content { background: #0f172a; border-right: 1px solid #1e293b; }
    h1 { font-family: 'Orbitron', sans-serif; color: #00f2fe; text-align: center; text-shadow: 0 0 10px #00f2fe; }
    .feature-card { background: #111827; border: 1px solid #1e293b; padding: 20px; border-radius: 15px; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR SETUP ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3413/3413535.png", width=100)
    st.title("🤖 ULTRA CORE")
    api_key = st.text_input("ENTER MASTER KEY (API):", type="password")
    mode = st.radio("SELECT MODE", [
        "🌐 Perplexity Search (Deep Research)", 
        "📑 Slide Deck Creator", 
        "📝 Pro Exam/Test", 
        "📊 Performance Manager",
        "🎙️ AI Tutor (Voice)"
    ])
    st.markdown("---")
    st.caption("Class 9 Ultimate Edition v2.0")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash') # Using Pro for smarter results

    # --- 1. PERPLEXITY SEARCH (Deep Research) ---
    if mode == "🌐 Perplexity Search (Deep Research)":
        st.write("### 🔍 World-Class Deep Research")
        query = st.text_input("Kya research karna hai? (E.g. Einstein's Theory or Mughal Empire)")
        if st.button("Deep Dive"):
            with st.spinner("Analyzing Global Data..."):
                prompt = f"Act as a combination of Perplexity and a PhD Tutor. Research {query} for a Class 9 student. Provide: 1. Core Concept 2. Real-world applications 3. Advanced Facts 4. Why it matters."
                res = model.generate_content(prompt)
                st.markdown(f"<div class='feature-card'>{res.text}</div>", unsafe_allow_html=True)

    # --- 2. SLIDE DECK CREATOR ---
    elif mode == "📑 Slide Deck Creator":
        st.write("### 🖼️ Presentation Slide Deck")
        topic = st.text_input("Presentation ka topic:")
        if st.button("Create Slides"):
            prompt = f"Create a slide-by-slide outline (Slide 1 to 10) for {topic}. Include bullet points for each slide and image suggestions."
            res = model.generate_content(prompt)
            st.code(res.text, language="markdown")

    # --- 3. PRO EXAM/TEST ---
    elif mode == "📝 Pro Exam/Test":
        st.write("### 🏁 Live Test Center")
        subj = st.selectbox("Subject", ["Physics", "Chemistry", "Math", "Bio"])
        if st.button("Start Grand Test"):
            prompt = f"Generate a high-level 10-question test for Class 9 {subj}. Mix MCQs and Short Questions. Don't give answers yet."
            res = model.generate_content(prompt)
            st.write(res.text)

    # --- 4. PERFORMANCE MANAGER ---
    elif mode == "📊 Performance Manager":
        st.write("### 📈 Student Progress Tracker")
        st.info("Coming Soon: Is section mein aapka progress graph save hoga!")
        marks = st.number_input("Last Test Marks (out of 100)", 0, 100)
        if st.button("Analyze My Level"):
            if marks > 80: st.success("Legend Level! You are ready to top.")
            else: st.warning("Thodi aur mehnat ki zaroorat hai, main madad karunga!")

    # --- 5. AI TUTOR (VOICE) ---
    elif mode == "🎙️ AI Tutor (Voice)":
        st.write("### 🔊 Talk to your Tutor")
        text_to_speak = st.text_area("Yahan wo topic likhen jo main parh kar sunaun:")
        if st.button("Read Aloud"):
            st.info("Ye feature aapki browser capability use karega.")
            st.markdown(f"<script>var msg = new SpeechSynthesisUtterance('{text_to_speak}'); window.speechSynthesis.speak(msg);</script>", unsafe_allow_html=True)

else:
    st.warning("⚠️ Access Denied: Please enter API Key in the sidebar.")
