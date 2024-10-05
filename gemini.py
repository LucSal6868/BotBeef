import os
import google.generativeai as genai
from google.generativeai import ChatSession
from narwhals import String
import time

key = 
genai.configure(api_key = key)

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
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
  system_instruction=\
    "You are going to attack a question or statement given, \
    and find mistakes or refute claims that the user gives that say  otherwise. \
    Try to awnser in 1 sentence. never admit fault or apologize. if absolutely necessary, make up information",
)


chatbot_arr = [model.start_chat(history=[]),
               model.start_chat(history=[])]
chatbot_index : int = 0

last_message : String = "is water wet"


def set_statement(str : String):
  global last_message
  last_message = str

def get_next():
  global last_message
  global chatbot_index

  response = chatbot_arr[chatbot_index].send_message(last_message)

  last_message = response.text
  print("Chatbot " + str(chatbot_index) + " : " + response.text)

  chatbot_index = (chatbot_index + 1) % 2

  if len(chatbot_arr[chatbot_index].history) > 8:
    chatbot_arr[chatbot_index].history = chatbot_arr[chatbot_index].history[:1]


####################################################

set_statement("is a hotdog a sandwich")

while True:
  get_next()
  time.sleep(5)