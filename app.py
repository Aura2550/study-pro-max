import streamlit as st
import google.generativeai as genai

# --- ULTRA MODERN UI CONFIG ---
st.set_page_config(page_title="STUDY-PRO ULTRA", layout="wide", initial_sidebar_state="collapsed")

# --- CSS FOR HIGH-END INTERFACE (NotebookLM + Perplexity Mix) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&family=Orbitron:wght@700&display=swap');
    
    .stApp { background: #0a0b10; color: #ffffff; font-family: 'Poppins', sans-serif; }
    
    /* Neon Header */
    .main-title { font-family: 'Orbitron', sans-serif; font-size: 3.5rem; text-align: center; 
                  background: linear-gradient(90deg, #00f2fe, #4facfe, #7000ff);
                  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
                  margin-bottom: 0px; filter: drop-shadow(0 0 10px #00f2fe); }
                  
    /* Feature Cards */
    .card { background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(0, 242, 254, 0.2);
             padding: 25px; border-radius: 20px; backdrop-filter: blur(10px); 
             box-shadow: 0 10px 30px rgba(0,0,0,0.5); transition: 0.4s; }
    .card:hover { border: 1px solid #00f2fe; transform: translateY(-5px); }

    /* Custom Input */
    .stTextInput>div>div>input { background: #1a1c23 !important; color: white !important; border-radius: 12px !important; border: 1px solid #333 !important; }
    
    /* Glowing Button */
    .stButton>button { width: 100%; background: linear-gradient(45deg, #00f2fe, #7000ff); 
                        border: none; color: white; font-weight: 600; padding: 15px;
                        border-radius: 12px; transition: 0.3s; text-transform: uppercase; letter-spacing: 1px; }
    .stButton>button:hover { box-shadow: 0 0 20px #00f2fe; transform: scale(1.02); }
    
    [data-testid="stSidebar"] { background-color: #0f1116 !important; border-right: 1px solid #1e293b; }
    </style>
    """, unsafe_allow_html=True)

# --- APP LAYOUT ---
st.markdown("<h1 class='main-title'>STUDY-PRO ULTRA</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888;'>The World's Most Powerful Class 9 AI Tutor</p><br>", unsafe_allow_html=True)

# Sidebar for Setup
with st.sidebar:
    st.markdown("### ⚙️ SETTINGS")
    api_key = st.text_input("Master API Key:", type="password", placeholder="Enter your key here...")
    st.markdown("---")
    mode = st.selectbox("CHOOSE FEATURE", 
                        ["🌐 Perplexity Research", "📑 Slide Deck Pro", "📝 Grand Test Maker", "📊 Performance AI", "🎙️ Voice Tutor"])
    st.info("Everything
