import streamlit as st
import gemini  # Ensure this is your gemini.py file
import time

# Initialize Streamlit session state
if 'bots_response' not in st.session_state:
    st.session_state.bots_response = []
if 'paused' not in st.session_state:
    st.session_state.paused = False

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
user_input = st.text_input("Enter a statement:")

st.markdown(
"""
Example Statements:
- Ketchup is a smoothie
- Water is wet
- A hot dog is a sandwich
- A poptart is a ravioli
- Cereal is a soup
- A straw only has 1 hole, not 2
"""
)

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
        width: 100%;  /* Set width to 100% */
        box-sizing: border-box;  /* Include padding and border in width */
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
    gemini.last_message = user_input
    index = 0
    while True:
        if st.session_state.paused:
            time.sleep(1)  # Check every second if paused
            continue

        # Generate a new response with alternating colors
        bot_response = gemini.get_next()  # Get the next bot's response
        color = colors[index % 2]
        styled_response = f'<div class="message-box {color}-box">Bot {index % 2 + 1}: {bot_response}</div>'        # Store the response in session state
        st.session_state.bots_response.append(styled_response)

        # Display the response with custom styling
        st.markdown(styled_response, unsafe_allow_html=True)

        index += 1
        time.sleep(5)

# Control buttons for chat, pause, and clear
spanner = False
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    if st.button("Chat", key="chatbutton"):
        spanner = True
        #start_beef()
        del st.session_state["chatbutton"]
with col2:
    if st.button("Pause", key="pausebutton"):
        st.session_state.paused = not st.session_state.paused  # Toggle pause state
with col3:
    if st.button("Clear", key="clearbutton"):
        st.session_state.bots_response = []  # Clear the chat history
        st.session_state.paused = False  # Reset pause state

if spanner is True:
    start_beef()


# Display bot responses in a separate full-width area
if st.session_state.bots_response:
    st.markdown("<hr>", unsafe_allow_html=True)  # Optional: Add a horizontal line before responses
    for response in st.session_state.bots_response:
        st.markdown(response, unsafe_allow_html=True)
