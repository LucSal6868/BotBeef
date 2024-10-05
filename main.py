import streamlit as st
import gemini  # Ensure this is your gemini.py file
import time

# Initialize Streamlit session state
if 'bots_response' not in st.session_state:
    st.session_state.bots_response = []
paused = False
starter = 0;

# Streamlit UI
st.title("⚔Beef Bots⚔️")
user_input = st.text_area("Enter a statement:", height=150)

def start_beef():
    index = 0
    while not paused:

        new_variable = gemini.get_next() + ":[blue]"
        if st.write(new_variable, key="next_response_button" + str(index)):  # Button to get the next response
            st.session_state.bots_response.append(new_variable)  # Store the next bot's response
        index += 1
        time.sleep(5)



if st.button("Chat"):
    start_beef()


# Pause button
if st.button("⏸️", key="pause_button"):  # Pause button with a pause symbol
    paused = True

# Continue conversation loop

# gemini.last_response = "Is ketchup a smoothie"

# Display bot responses
for response in st.session_state.bots_response:
    st.write(response)
