# main.py

import streamlit as st
import gemini  # Import the gemini module

# Set up the title and page configuration
st.set_page_config(page_title="BotBeef", page_icon="🤖", layout="centered")

# Title and subheader with dark mode style
st.markdown("""
    <style>
        .main-title {
            color: #f0f0f0;
            text-align: center;
            font-size: 3rem;
        }
        .sub-title {
            color: #a3a3a3;
            text-align: center;
            margin-bottom: 20px;
        }
        .pause-icon {
            background-color: transparent;
            color: #aaa;
            font-size: 1.5rem;
            cursor: pointer;
            margin-left: 10px;
            position: relative;
            top: 50%;
            transform: translateY(-50%);
        }
        .chat-textbox {
            background-color: #444;
            color: #f0f0f0;
            border: 1px solid #555;
            border-radius: 10px;
            padding: 10px;
            font-size: 1rem;
            width: 100%;
            min-height: 50px;
            resize: vertical;  /* Allow vertical resizing */
            overflow-y: auto;
        }
        .chat-input-container {
            display: flex;
            align-items: center;
            position: relative;
            width: 100%;
        }
        .timer {
            position: absolute;
            top: 10px;
            right: 10px;
            background-color: #444;
            padding: 10px 20px;
            border-radius: 5px;
            color: #f0f0f0;
        }
    </style>
    """, unsafe_allow_html=True)

# Display title and subheader
st.markdown("<h1 class='main-title'>🤖🍖 BotBeef 🍖🤖</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='sub-title'>Watch two chatbots go head-to-head in a battle of wits!</h3>", unsafe_allow_html=True)

# Growing text input for user question with a pause button (inside text box)
st.markdown("<p style='color: #f0f0f0;'>Ask your question or provide a statement to start the debate:</p>", unsafe_allow_html=True)

input_container = st.container()
with input_container:
    chat_input = st.text_area("", "", height=100, max_chars=500, key="user_input", placeholder="Type your question here...", help="Type your question here...")
    st.markdown("""
        <div class="chat-input-container">
            <span class="pause-icon">⏸</span>
        </div>
        """, unsafe_allow_html=True)

# Submit button for user input
if st.button("Submit"):
    user_input = st.session_state.user_input
    if user_input:
        # Get the response from the gemini module
        response_a = gemini.get_response(user_input)
        response_b = gemini.get_response(user_input)

        # Display chatbot responses
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"""
                <div style='background-color: #333; padding: 20px; border-radius: 10px;'>
                    <h4 style='color: #f0f0f0;'>🤖 <strong>Chatbot A</strong></h4>
                    <p style='color: #b0b0b0;'>{response_a}</p>
                </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
                <div style='background-color: #333; padding: 20px; border-radius: 10px;'>
                    <h4 style='color: #f0f0f0;'>🤖 <strong>Chatbot B</strong></h4>
                    <p style='color: #b0b0b0;'>{response_b}</p>
                </div>
            """, unsafe_allow_html=True)


