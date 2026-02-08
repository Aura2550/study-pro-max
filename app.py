import streamlit as st
import requests
import json

# Minimal UI for Maximum Speed
st.set_page_config(page_title="STUDY-PRO QUICK", layout="wide")
st.title("🎓 STUDY-PRO BEYOND (Quick Fix)")

# Sidebar
with st.sidebar:
    api_key = st.text_input("ENTER API KEY:", type="password")
    mode = st.selectbox("MODULE:", ["Research", "Exam", "Slides"])

# Logic
if api_key:
    topic = st.text_input("Enter Topic (e.g., Atom):")
    if st.button("RUN"):
        # Direct API Call
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
        data = {"contents": [{"parts": [{"text": f"Explain {topic} for Class 9 in detail. Mode: {mode}"}]}]}
        
        try:
            res = requests.post(url, json=data, timeout=15)
            output = res.json()['candidates'][0]['content']['parts'][0]['text']
            
            # Displaying result in a clean box
            st.success("Mission Success!")
            st.text_area("Result:", value=output, height=400)
            
            # Quick Diagram Check
            t = topic.lower()
            if "heart" in t:
                st.write("### 📊 Visual Reference")
                st.markdown("

[Image of the human heart anatomy]
")
            elif "cell" in t:
                st.write("### 📊 Visual Reference")
                st.markdown("

[Image of plant and animal cell]
")
            elif "atom" in t:
                st.write("### 📊 Visual Reference")
                st.markdown("

[Image of Bohr's atomic model]
")

        except Exception as e:
            st.error(f"Error: {e}")
else:
    st.warning("Sidebar mein Key daalein.")
