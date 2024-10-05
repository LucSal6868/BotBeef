import streamlit as st
import time

# Set up the title and page configuration
st.set_page_config(page_title="BotBeef", page_icon="🤖", layout="centered")

# Function to display the self-destruct timer
def self_destruct_timer():
    countdown_time = 300  # 5 minutes
    time_left = countdown_time - (time.time() - start_time)

    # Display the timer in the top right corner
    st.markdown(f"""
    <div style='position: absolute; top: 10px; right: 10px; background-color: #444; padding: 10px 20px; border-radius: 5px;'>
        <p style='color: #f0f0f0;'>Self-Destruct in: {int(time_left // 60)}:{int(time_left % 60):02}</p>
    </div>
    """, unsafe_allow_html=True)

    return time_left

# Start the timer at the moment the app is launched
start_time = time.time()

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
            position: absolute;
            right: 10px;
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
            max-height: 200px;
            overflow-y: auto;
            resize: none;
        }
        .chat-input-container {
            display: flex;
            align-items: center;
            position: relative;
            width: 100%;
        }
    </style>
    """, unsafe_allow_html=True)

# Display title and subheader
st.markdown("<h1 class='main-title'>🤖🍖 BotBeef 🍖🤖</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='sub-title'>Watch two chatbots go head-to-head in a battle of wits!</h3>", unsafe_allow_html=True)

# Growing text input for user question with a pause button (inside text box)
st.markdown("<p style='color: #f0f0f0;'>Ask your question or provide a statement to start the debate:</p>", unsafe_allow_html=True)

st.markdown("""
    <div class="chat-input-container">
        <textarea class="chat-textbox" placeholder="Type your question here..."></textarea>
        <span class="pause-icon">⏸</span>
    </div>
    """, unsafe_allow_html=True)

# Placeholder for chatbot responses
st.markdown("### Chatbot Showdown 🥊")
col1, col2 = st.columns(2)

# Personalities for chatbots
personalities = ["Snarky", "Logical", "Pessimistic", "Optimistic", "Delusional", "Chronic Liar",
                 "Friendly", "Overly Confident", "Insecure"]

with col1:
    personality_a = st.selectbox("Choose Chatbot A's Personality:", personalities, index=1)
    st.markdown(f"""
        <div style='background-color: #333; padding: 20px; border-radius: 10px;'>
            <h4 style='color: #f0f0f0;'>🤖 <strong>Chatbot A</strong> ({personality_a} Mode)</h4>
            <p style='color: #b0b0b0;'>Waiting for argument...</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    personality_b = st.selectbox("Choose Chatbot B's Personality:", personalities, index=0)
    st.markdown(f"""
        <div style='background-color: #333; padding: 20px; border-radius: 10px;'>
            <h4 style='color: #f0f0f0;'>🤖 <strong>Chatbot B</strong> ({personality_b} Mode)</h4>
            <p style='color: #b0b0b0;'>Waiting for counter-argument...</p>
        </div>
    """, unsafe_allow_html=True)

# Divider for styling
st.markdown("<hr style='border-top: 2px solid #444;' />", unsafe_allow_html=True)

# Footer or fun message
st.markdown("<p style='text-align: center; color: #a3a3a3;'>Ready for the beef? Let's get debating! 🍿</p>", unsafe_allow_html=True)

# Display the self-destruct timer at the top right corner
timeLeft = self_destruct_timer()

# Stop the app once the self-destruct timer reaches 0
if timeLeft <= 0:
    st.error("💥 The app has self-destructed! Refresh the page to start again.")
    st.stop()
