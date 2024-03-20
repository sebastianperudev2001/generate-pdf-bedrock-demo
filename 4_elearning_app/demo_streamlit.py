import streamlit as st
import requests

st.title("Azure Chatbot Study Guide")

# Input field for user question
user_input = st.text_input("Ask a question about Azure:")

# Button to submit the question
submit_button = st.button("Submit")

if submit_button and user_input:
    # Define API endpoint URL
    url = "https://yrj0xmfygj.execute-api.us-east-1.amazonaws.com/dev"

    # Send POST request with user question
    params = {
        "prompt": user_input  # Replace with your prompt value
    }
    response = requests.get(url, params=params)

    # Parse JSON response
    if response.status_code == 200:
        bedrock_response = response.json().get("body")
        st.text_area("Chatbot Response:", value=bedrock_response, height=200, max_chars=None, key=None)
    else:
        st.error("Error: Failed to get response from API")
