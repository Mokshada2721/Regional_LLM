import streamlit as st
import requests

# Specify the endpoint where you want to send the feedback
FEEDBACK_ENDPOINT = "YOUR_FEEDBACK_ENDPOINT"

def send_feedback(feedback_text):
    # Send the feedback to the specified endpoint
    payload = {"feedback": feedback_text}
    response = requests.post(FEEDBACK_ENDPOINT, json=payload)
    if response.status_code == 200:
        return True
    else:
        return False

st.title("User Feedback")

feedback_text = st.text_area("Provide your feedback here:")

if st.button("Submit Feedback"):
    if feedback_text:
        if send_feedback(feedback_text):
            st.success("Feedback submitted successfully!")
        else:
            st.error("Failed to submit feedback. Please try again later.")
    else:
        st.warning("Please enter your feedback before submitting.")
