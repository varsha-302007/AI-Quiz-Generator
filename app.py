import streamlit as st
import google.generativeai as genai

# Configure API
api_key = st.secrets["AIzaSyDON77QqwQLX-tFPzqDhhYUtYV_FIqIa6o"]

genai.configure(api_key=api_key)

# Load model
model = genai.GenerativeModel("gemini-flash-latest")

# Streamlit UI
st.title("AI Quiz Generator")

topic = st.text_input("Enter Topic")

if st.button("Generate Quiz"):

    if topic:

        prompt = f"Create 5 multiple choice questions about {topic}"

        response = model.generate_content(prompt)

        st.write(response.text)

    else:
        st.warning("Please enter a topic")