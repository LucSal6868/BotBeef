import streamlit as st

st.set_page_config(page_title="BotBeef", page_icon="🤖", layout="centered")

st.title("🤖🍖 BotBeef 🍖🤖")

st.subheader("Watch two chatbots go head-to-head in a battle of wits!")

user_input = st.text_input("Ask your question or provide a statement to start the debate:")

st.markdown("### Chatbot Showdown 🥊")
col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 🤖 **Chatbot A** (Argument A)")
    st.markdown("Waiting for argument...")

with col2:
    st.markdown("#### 🤖 **Chatbot B** (Argument B)")
    st.markdown("Waiting for counter-argument...")

st.markdown("---")

st.markdown("""
    <style>
        .stTextInput > div > div > input {
            border: 2px solid #ff4b4b;  /* Red border for the input field */
            padding: 10px;
        }
        .stMarkdown h4 {
            color: #ff4b4b;  /* Red for the chatbot titles */
        }
        .stMarkdown {
            background-color: #f0f0f5; /* Light background for chatbot responses */
            border-radius: 10px;
            padding: 15px;
            margin: 10px;
        }
    </style>
    """, unsafe_allow_html=True)

st.markdown("### Ready for the beef? Let's get debating! 🍿")
