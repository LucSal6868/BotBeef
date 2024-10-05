import streamlit as st

st.set_page_config(page_title="BotBeef", page_icon="🤖", layout="centered")

st.markdown("""
    <style>
        .main-title {
            color: #f0f0f0; /* Light color for the main title */
            text-align: center;
            font-size: 3rem;
        }
        .sub-title {
            color: #a3a3a3; /* Lighter subheader text */
            text-align: center;
            margin-bottom: 20px;
        }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>🤖🍖 BotBeef 🍖🤖</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='sub-title'>Watch two chatbots go head-to-head in a battle of wits!</h3>", unsafe_allow_html=True)

st.markdown("<p style='color: #f0f0f0;'>Ask your question or provide a statement to start the debate:</p>", unsafe_allow_html=True)
user_input = st.text_input("")

personalities = ["Snarky", "Logical", "Pessimistic", "Optimistic", "Delusional", "Chronic Liar",
                 "Friendly", "Overly Confident", "Insecure"]

col1, col2 = st.columns(2)

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

st.markdown("<hr style='border-top: 2px solid #444;' />", unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color: #a3a3a3;'>Ready for the beef? Let's get debating! 🍿</p>", unsafe_allow_html=True)

# dark mode styling
st.markdown("""
    <style>
        .stTextInput > div > div > input {
            background-color: #444;
            color: #f0f0f0;
            border: 1px solid #555;  /* Darker border for input field */
            padding: 10px;
        }
        .stMarkdown h4 {
            color: #f0f0f0;  /* Light color for chatbot titles */
        }
        .stMarkdown p {
            color: #b0b0b0;  /* Light gray text */
        }
        .stMarkdown {
            background-color: #333; /* Dark background for chatbot areas */
            border-radius: 10px;
            padding: 15px;
            margin: 10px;
        }
        .stTextInput {
            background-color: #444;
        }
        body {
            background-color: #222; /* Dark mode background */
        }
    </style>
    """, unsafe_allow_html=True)
