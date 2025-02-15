# azure.py
# Import necessary libraries
import streamlit as st
import openai
import os
# Set up your OpenAI API key
openai.api_key = os.environ.get('OPENAI_API_KEY')
# Initialize Streamlit
st.title("Massachusetts Legal Guide Chatbot")
# Create a text input field for user queries
user_input = st.text_input("Ask a legal question about Massachusetts:")
# Send the user's query to OpenAI GPT-3
if user_input:
    response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=user_input,
    max_tokens=50,
    temperature=0.2    
    )
    st.write(response['choices'][0]['text'].strip())
