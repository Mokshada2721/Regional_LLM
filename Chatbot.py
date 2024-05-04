import streamlit as st
import requests
from langdetect import detect

API_URL = "https://api-inference.huggingface.co/models/l3cube-pune/marathi-gpt"
HEADERS = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    return response.json()

def remove_english_words(text):
    # Detect the language of the text
    language = detect(text)
    # If the detected language is English, remove English words
    if language == "en":
        # Define English alphabet characters
        english_alphabet = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        # Filter out English words
        filtered_text = "".join([char for char in text if char not in english_alphabet])
        return filtered_text
    else:
        return text


def generate_response(prompt):
    max_input_length = 50  # Maximum allowed input length
    prompt = remove_english_words(prompt)
    prompt = prompt[:max_input_length]  # Take only the first max_input_length characters
    #prompt += " summarize"  # Add "summarize" to the prompt if summarization is requested
    output = query({"inputs": prompt})
    return output[0]['generated_text'] if output and isinstance(output, list) and len(output) > 0 else None


st.title("💬 Vachanakar")
st.caption("🚀 A streamlit chatbot powered by Hugging Face's Marathi GPT")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = generate_response(prompt)
    if response:
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.chat_message("assistant").write(response)
    else:
        st.error("Error: Unable to generate response")