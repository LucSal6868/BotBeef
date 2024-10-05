import streamlit as st
import gemini  # Ensure this is your gemini.py file
import time
import  random

# Initialize Streamlit session state
if 'bots_response' not in st.session_state:
    st.session_state.bots_response = []
paused = False
starter = 0;

#Questions premade
questions = ["Ketchup is a smoothie",
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

def start_beef():
    index = 0
    while not paused:
        new_variable : str = f":{colors[index % 2]}[" + gemini.get_next() +"]"
        if st.write(new_variable, key="next_response_button" + str(index)):  # Button to get the next response
            st.session_state.bots_response.append(new_variable)  # Store the next bot's response
        index += 1


        time.sleep(5)



if st.button("Chat", key="chatbutton"):
    start_beef()
    del st.session_state["chatbutton"]


# Pause button
if st.button("⏸️", key="pause_button"):  # Pause button with a pause symbol
    #paused = True
    pass

# Continue conversation loop

# gemini.last_response = "Is ketchup a smoothie"

# Display bot responses
for response in st.session_state.bots_response:
    st.write(response)
