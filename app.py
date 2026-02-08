import streamlit as st
import requests
import json

# --- 1. CONFIG ---
st.set_page_config(page_title="STUDY-PRO BEYOND v12.0", layout="wide")

# --- 2. ULTIMATE CSS (FIXED & TESTED) ---
st.markdown("""
    <style>
    .stApp { background: #010409; color: #e6edf3; font-family: 'Segoe UI', sans-serif; }
    .hero-title { font-size: 3rem; text-align: center; color: #58a6ff; font-weight: bold; padding: 20px; }
    .main-card { background: #161b22; border: 1px solid #30363d; padding: 25px; border-radius: 15px; margin-bottom: 20px; }
    .stButton>button { background: linear-gradient(45deg, #238636, #2ea043); color: white; border-radius: 8px; border: none; padding: 12px; font-weight: bold; width: 100%; }
    .stTextInput>div>div>input { background: #0d1117 !important; color: white !important; border: 1px solid #30363d !important; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='hero-title'>STUDY-PRO BEYOND v12.0</h1>", unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    st.header("⚙️ ACCESS CONTROL")
    api_key = st.text_input("ENTER MASTER KEY:", type="password")
    mode = st.selectbox("SELECT MODULE:", ["🌐 Deep Research", "📝 Exam Architect", "📑 Slide Deck"])
    st.markdown("---")
    st.success("Engine: Requests-Direct")

# --- 4. DIRECT ENGINE ---
def call_gemini(key, prompt):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={key}"
    headers = {'Content-Type': 'application/json'}
    data = {"contents": [{"parts": [{"text": prompt}]}]}
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data), timeout=15)
        res_json = response.json()
        if 'candidates' in res_json:
            return res_json['candidates'][0]['content']['parts'][0]['text']
        else:
            return f"Error: {res_json.get('error', {}).get('message', 'Check API Key')}"
    except Exception as e:
        return f"System Error: {str(e)}"

# --- 5. WORKSPACE ---
if api_key:
    st.markdown("<div class='main-card'>", unsafe_allow_html=True)
    topic = st.text_input("Enter your Study Topic:")
    run_btn = st.button("LAUNCH MISSION")
    st.markdown("</div>", unsafe_allow_html=True)

    if run_btn and topic:
        with st.spinner("Neural Link Active..."):
            if mode == "🌐 Deep Research":
                p = f"Explain {topic} for Class 9 in detail with bullet points."
            elif mode == "📝 Exam Architect":
                p = f"Create a Class 9 test for {topic} with answers."
            else:
                p = f"Create a 7-slide outline for {topic}."

            output = call_gemini(api_key, p)
            
            st.markdown("### 📥 RESULT")
            st.markdown(f"<div class='main-card'>{output}</div>", unsafe_allow_html=True)
            
            # Smart Visual Tags
            t_low = topic.lower()
            if "heart" in t_low:
                st.write("### 📊 Diagram Reference")
                st.markdown("

[Image of the human heart anatomy]
")
            elif "cell" in t_low:
                st.write("### 📊 Diagram Reference")
                st.markdown("

[Image of animal cell vs plant cell]
")
            elif "atom" in t_low:
                st.write("### 📊 Diagram Reference")
                st.markdown("

[Image of Bohr's atomic model]
")
            elif "digestive" in t_low:
                st.write("### 📊 Diagram Reference")
                st.markdown("

[Image of the human digestive system]
")
else:
    st.warning("⚠️ Access Denied: Please enter API Key in sidebar.")
