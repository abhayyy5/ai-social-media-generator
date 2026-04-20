import streamlit as st
from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

st.title("📱 AI Social Media Content Generator")

topic = st.text_input("Enter Topic")
platform = st.selectbox("Platform", ["Instagram", "LinkedIn", "Twitter"])
tone = st.selectbox("Tone", ["Motivational", "Funny", "Professional"])

if st.button("Generate Post"):
    prompt = f"Write a {tone} social media post for {platform} about {topic}. Include hashtags."

    result = generator(prompt, max_length=100, num_return_sequences=1)

    st.write(result[0]['generated_text'])
