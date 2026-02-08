import streamlit as st
import requests
import json

# --- CONFIG ---
st.set_page_config(page_title="STUDY-PRO BEYOND v11.0", layout="wide")

# --- EXTREME CSS ---
st.markdown("""
    <style>
    .stApp { background: #010409; color: #e6edf3; }
    .hero-title { font-size: 3.5rem; text-align: center; color: #58a6ff; font-weight: bold; }
    .main-card { background: #161b22; border: 1px solid #30363d; padding: 25px; border-radius: 15px; }
    .stButton>button { background: linear-gradient(45deg, #238636, #2ea043); color: white; font-weight: bold; border: none; padding: 12px; width: 100%; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='hero-title'>STUDY-PRO BEYOND</h1>", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.header("⚙️ ACCESS CONTROL")
    api_key = st.text_input("ENTER MASTER KEY:", type="password")
    mode = st.selectbox("SELECT MODULE:", ["🌐 Deep Research", "📝 Exam Architect", "📑 Slide Deck"])

# --- ENGINE ---
def call_neural_engine(key, prompt):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={key}"
    headers = {'Content-Type': 'application/json'}
    data = {"contents": [{"parts": [{"text": prompt}]}]}
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data), timeout=15)
        res_json = response.json()
        if 'candidates' in res_json:
            return res_json['candidates'][0]['content']['parts'][0]['text']
        return f"ERROR: {res_json.get('error', {}).get('message', 'Key Invalid')}"
    except Exception as e:
        return f"System Error: {str(e)}"

# --- WORKSPACE ---
if api_key:
    st.markdown("<div class='main-card'>", unsafe_allow_html=True)
    topic = st.text_input("Enter Topic (e.g., Structure of Atom):")
    execute = st.button("LAUNCH ENGINE")
    st.markdown("</div>", unsafe_allow_html=True)

    if execute and topic:
        with st.spinner("Processing..."):
            if mode == "🌐 Deep Research":
                p = f"Explain {topic} for Class 9 in detail with headings."
            elif mode == "📝 Exam Architect":
                p = f"Create a Class 9 Exam for {topic} with answers."
            else:
                p = f"Create a slide deck outline for {topic}."

            output = call_neural_engine(api_key, p)
            
            st.markdown("### 📥 OUTPUT")
            st.markdown(f"<div class='main-card'>{output}</div>", unsafe_allow_html=True)
            
            # Smart Diagrams Section (Fixed Syntax)
            t_low = topic.lower()
            if "heart" in t_low:
                st.write("### 📊 Visual Reference")
                st.markdown("

[Image of the human heart anatomy]
")
            elif "cell" in t_low:
                st.write("### 📊 Visual Reference")
                st.markdown("

[Image of animal cell vs plant cell]
")
            elif "atom" in t_low:
                st.write("### 📊 Visual Reference")
                st.markdown("

[Image of Bohr's atomic model]
")
else:
    st.warning("Please enter your API Key in the sidebar.")
