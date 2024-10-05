# gemini.py

import os
import google.generativeai as genai
from google.generativeai import ChatSession
from narwhals import String

API_KEY = "AIzaSyCRUQPmk2oJWiQIa9f0m34VHKGAGHDiYNw"
genai.configure(api_key=API_KEY)

# Create the model
generation_config = {
    "temperature": 1,
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
)

chatbot_arr = [model.start_chat(history=[]),
                model.start_chat(history=[])]
chatbot_index = 0

def get_response(statement):
    global chatbot_index

    response = chatbot_arr[chatbot_index].send_message(statement)
    answer = response.text

    chatbot_index = (chatbot_index + 1) % 2  # Switch between chatbots

    # Maintain a history limit
    if len(chatbot_arr[chatbot_index].history) > 8:
        chatbot_arr[chatbot_index].history = chatbot_arr[chatbot_index].history[:1]

    return answer
