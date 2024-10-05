import streamlit as st
import gemini  # Ensure this is your gemini.py file
import time
import random

# Initialize Streamlit session state
if 'bots_response' not in st.session_state:
    st.session_state.bots_response = []
paused = False

# Pre-made questions
questions = [
    "Ketchup is a smoothie",
    "Water is wet",
    "A hot dog is a sandwich",
    "A poptart is a ravioli",
    "Cereal is a soup",
    "A straw only has 1 hole, not 2"
]

# Streamlit UI
st.title("⚔ Beef Bots ⚔")
user_input = st.text_input("Enter a statement:", random.choice(questions))

colors = ["red", "blue"]

# Custom CSS for chatbot messages
st.markdown(
    """
    <style>
    .message-box {
        padding: 10px;
        margin: 10px 0;
        border-radius: 10px;
        border: 2px solid;
        width: fit-content;
    }
    .red-box {
        border-color: red;
        background-color: #8B0000;
    }
    .blue-box {
        border-color: blue;
        background-color: #00008B;
    }
    </style>
    """, unsafe_allow_html=True
)


def start_beef():
    index = 0
    while not paused:
        # Generate a new response with alternating colors
        bot_response = gemini.get_next()  # Get the next bot's response
        color = colors[index % 2]
        styled_response = f'<div class="message-box {color}-box">Bot {index % 2 + 1}: {bot_response}</div>'

        # Display the response with custom styling
        st.markdown(styled_response, unsafe_allow_html=True)

        # Store the response in session state
        st.session_state.bots_response.append(styled_response)

        index += 1
        time.sleep(5)


if st.button("Chat", key="chatbutton"):
    start_beef()
    del st.session_state["chatbutton"]

# Pause button
if st.button("⏸️", key="pause_button"):  # Pause button with a pause symbol
    # paused = True
    pass

# Display bot responses
for response in st.session_state.bots_response:
    st.markdown(response, unsafe_allow_html=True)
