# gemini.py

import os
import google.generativeai as genai
import streamlit as st
from google.generativeai import ChatSession
from narwhals import String
from google.generativeai.types import HarmCategory, HarmBlockThreshold

API_KEY = st.secrets["API_KEY"]
genai.configure(api_key=API_KEY)

# Create the model
generation_config = {
    "temperature": 2,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 64,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction=(
        "You are going to attack a question or statement given, "
        "and find mistakes or refute claims that the user gives that say otherwise. "
        "Try to answer in 1 sentence. Never admit fault or apologize. "
        "If absolutely necessary, make up information."
    ),

    safety_settings={
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
        # HarmCategory.HARM_CATEGORY_UNSPECIFIED: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
    }
)

chatbot_arr = [model.start_chat(history=[]),
                model.start_chat(history=[])]
chatbot_index = 0

last_message: str = "Is ketchup a drink"

def get_next():
    global last_message
    global chatbot_index

    # Generate response from the current bot
    response = chatbot_arr[chatbot_index].send_message(last_message)
    last_message = response.text

    # Print the response for debugging
    print("Chatbot " + str(chatbot_index) + " : " + response.text)

    # Switch to the next chatbot for the next turn
    chatbot_index = (chatbot_index + 1) % 2

    # Limit the history length for the current bot
    if len(chatbot_arr[chatbot_index].history) > 8:
        chatbot_arr[chatbot_index].history = chatbot_arr[chatbot_index].history[:1]

    return last_message  # Return the last message for displaying it in the UI
