import streamlit as st
import torch
from transformers import pipeline, AutoModelForSeq2SeqLM, AutoTokenizer
import time

# Loading the model
model_path = "E:\\Git Uploads\\English-to-Spanish-Translation-APP\\notebook\\results\\checkpoint-28041"
model = AutoModelForSeq2SeqLM.from_pretrained(model_path).to("cuda")
tokenizer = AutoTokenizer.from_pretrained(model_path)

# Translation pipeline
translator = pipeline("translation_en_to_es", model=model, tokenizer=tokenizer, device=0)

# Streamlit app
st.title("English to Spanish Translator")
st.write("Translate your English text into Spanish instantly!")

# Text input for user to enter English text
with st.sidebar:
    st.header("Input Text")
    text_input = st.text_area("Enter your English text here:")

if st.button("Translate"):
    if text_input:
        # Create a progress bar
        progress_bar = st.progress(0)
        progress_text = st.empty()
        
        for i in range(100):
            # Update progress bar and text
            progress_bar.progress(i + 1)
            progress_text.text(f"Translating... {i+1}%")
            time.sleep(0.05)  # Simulate translation time (adjust as needed)

        # Translate the input text
        translation = translator(text_input)[0]["translation_text"]

        # Display the translation
        progress_bar.empty()
        progress_text.empty()
        st.success("Spanish Translation:")
        st.info(translation)

    else:
        st.warning("Please enter some text to translate.")

st.markdown("""
<style>
.stApp {
    background-color: #f5f5f5;
}
.stTextInput > textarea {
    height: 200px;  # Adjust text area height
}
</style>
""", unsafe_allow_html=True)

