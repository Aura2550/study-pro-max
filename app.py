import streamlit as st
import requests

st.title("STUDY-PRO ULTRA MAX")

# Sidebar for Key
key = st.sidebar.text_input("API KEY", type="password")
mode = st.sidebar.selectbox("MODE", ["Research", "Exam", "Slides"])

# Simple Input
topic = st.text_input("Enter Topic:")

if st.button("RUN"):
    if key and topic:
        # Direct API Call without any complex formatting
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={key}"
        payload = {"contents": [{"parts": [{"text": f"Class 9 level {mode} on {topic}. Give detailed notes and questions."}]}]}
        
        try:
            r = requests.post(url, json=payload)
            data = r.json()
            # Direct text display - NO CSS TO BREAK IT
            content = data['candidates'][0]['content']['parts'][0]['text']
            st.write(content)
            
            # Diagram placeholders for your visual help
            if "heart" in topic.lower():
                st.write("### 

[Image of the human heart anatomy]
")
            elif "atom" in topic.lower():
                st.write("### 

[Image of Bohr's atomic model]
")
                
        except Exception as e:
            st.error("Check your API Key or Internet.")
    else:
        st.warning("Please enter both Key and Topic.")
