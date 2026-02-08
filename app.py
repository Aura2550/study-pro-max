import streamlit as st
import requests
import json

# --- ULTRA MODERN UI ---
st.set_page_config(page_title="STUDY-PRO BEYOND", layout="wide")
st.markdown("""
    <style>
    .stApp { background: #010409; color: white; }
    .card { background: #161b22; border: 1px solid #58a6ff; padding: 25px; border-radius: 15px; margin-top: 20px; }
    .title { color: #58a6ff; text-align: center; font-size: 3rem; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='title'>STUDY-PRO BEYOND</h1>", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.header("⚙️ SETTINGS")
    api_key = st.text_input("ENTER API KEY:", type="password")
    mode = st.radio("TOOL:", ["Research", "Exam", "Slides"])

# --- DIRECT API CALL FUNCTION ---
def call_gemini_direct(key, prompt):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={key}"
    headers = {'Content-Type': 'application/json'}
    data = {
        "contents": [{"parts": [{"text": prompt}]}]
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()

# --- MAIN LOGIC ---
if api_key:
    topic = st.text_input("Enter Topic:")
    if st.button("RUN ENGINE"):
        if not topic:
            st.warning("Please enter a topic!")
        else:
            with st.spinner("Connecting to Google Servers..."):
                try:
                    # Specific prompts based on mode
                    final_prompt = f"Explain {topic} for Class 9."
                    if mode == "Exam":
                        final_prompt = f"Create a Class 9 test for {topic} with answers."
                    elif mode == "Slides":
                        final_prompt = f"Create a 7-slide outline for {topic}."

                    result = call_gemini_direct(api_key, final_prompt)
                    
                    # Extracting text safely
                    if 'candidates' in result:
                        output_text = result['candidates'][0]['content']['parts'][0]['text']
                        st.markdown(f"<div class='card'>{output_text}</div>", unsafe_allow_html=True)
                    else:
                        st.error(f"API Error: {result.get('error', {}).get('message', 'Unknown Error')}")
                        st.info("Tip: Make sure you copied the NEW API key correctly.")
                except Exception as e:
                    st.error(f"System Error: {e}")
else:
    st.warning("Sidebar mein API Key daalein.")
