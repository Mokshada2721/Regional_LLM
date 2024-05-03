import streamlit as st
import requests

API_URL = "https://api-inference.huggingface.co/models/l3cube-pune/marathi-gpt"
HEADERS = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    return response.json()

st.title("💬 Vachanakar")
st.caption("🚀 A chatbot to summarize text in Marathi")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    output = query({"inputs": prompt})
    st.write("Response from Hugging Face API:", output)  # Print the output for debugging
    if output and 'generated_text' in output[0]:
        msg = output[0]['generated_text']
        st.session_state.messages.append({"role": "assistant", "content": msg})
        st.chat_message("assistant").write(msg)
    else:
        st.error("Error: Unable to generate response")