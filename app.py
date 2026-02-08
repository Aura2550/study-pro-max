import streamlit as st
import google.generativeai as genai

# --- UI CONFIG ---
st.set_page_config(page_title="STUDY-PRO BEYOND v9.0", layout="wide")
st.markdown("""<style>
    .stApp { background: #010409; color: white; }
    .result-box { background: #161b22; border: 2px solid #58a6ff; padding: 25px; border-radius: 15px; }
    .title { color: #58a6ff; font-weight: bold; font-size: 3rem; text-align: center; }
</style>""", unsafe_allow_html=True)

st.markdown("<h1 class='title'>STUDY-PRO BEYOND (FORCE MODE)</h1>", unsafe_allow_html=True)

with st.sidebar:
    api_key = st.text_input("ENTER MASTER KEY:", type="password")
    mode = st.selectbox("MODULE", ["Research", "Exam", "Slides"])

# --- BYPASS ENGINE ---
if api_key:
    try:
        genai.configure(api_key=api_key)
        
        # 1. DISABLE ALL SAFETY FILTERS (Block hatao)
        safety_settings = [
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
        ]

        # 2. SELECT MODEL (Try Flash first, then Pro)
        try:
            model = genai.GenerativeModel('gemini-1.5-flash', safety_settings=safety_settings)
            # Test call
            model.generate_content("hi")
        except:
            model = genai.GenerativeModel('gemini-pro', safety_settings=safety_settings)

        st.success("⚡ NEURAL LINK: BYPASS ACTIVE!")
        
        topic = st.text_input("Enter Topic (e.g., Structure of Atom):")
        if st.button("EXECUTE MISSION"):
            with st.spinner("AI is forcing connection..."):
                prompt = f"Act as a pro teacher. Explain {topic} for Class 9 student in detail with headings."
                if mode == "Exam":
                    prompt = f"Create a Class 9 test for {topic} with answers."
                
                res = model.generate_content(prompt)
                st.markdown(f"<div class='result-box'>{res.text}</div>", unsafe_allow_html=True)

    except Exception as e:
        st.error(f"FATAL ERROR: {e}")
        st.info("Bhai, agar ab bhi nahi chala, toh iska matlab hai aapki API Key 'Restricted' hai. Ek baar Google AI Studio mein 'Chat' karke dekho, wahan koi Error toh nahi aa raha?")
else:
    st.warning("Please enter API Key in the sidebar.")
