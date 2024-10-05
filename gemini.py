import os
import google.generativeai as genai

API_KEY = os.getenv("API_KEY")

genai.configure(api_key=os.environ[API_KEY])

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
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
  system_instruction="You are going to defend a question or statement given, and find mistakes or refute claims that the use gives that say  otherwise. Try to awnser in 1 to 2 sentences. ",
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "water is wet",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Water is a liquid, and liquids are defined by their ability to flow and take the shape of their container. This property of flow makes water feel wet to the touch. \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "but water cant be wet",
      ],
    },
    {
      "role": "model",
      "parts": [
        "This statement is incorrect. Wetness is a sensation caused by the interaction of a liquid with a surface, and water, being a liquid, can certainly cause this sensation. \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "water is made of molecules, which arent wet",
      ],
    },
    {
      "role": "model",
      "parts": [
        "While water is made of molecules, the concept of \"wetness\" applies to the macroscopic level, not the molecular level. Wetness is a sensation experienced by a surface interacting with a liquid, not an inherent property of the individual molecules themselves. \n",
      ],
    },
  ]
)

response = chat_session.send_message("INSERT_INPUT_HERE")

print(response.text)