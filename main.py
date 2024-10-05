from operator import index

import streamlit as st
from attr.validators import disabled

import gemini  # Ensure this is your gemini.py file
import time
import  random



#Questions premade
questions = ["Ketchup is a smoothie",
             "Water is wet",
             "A hot dog is a sandwich",
             "A poptart is a ravioli",
             "Cereal is a soup",
             "A straw only has 1 hole, not 2",
             "The Chicken came first and not the egg"
             ]

# Streamlit UI
st.title("⚔ Beef Bots ⚔")
user_input = st.text_input("Enter a statement:", random.choice(questions))

colors = ["red", "blue"]
paused = False

def start_beef():
    gemini.last_message = user_input
    index = 0
    while not paused:
        new_variable : str = f":{colors[index % 2]}[" + gemini.get_next() +"]"
        st.write(new_variable, key="next_response_button" + str(index))  # text to get the next response


        index += 1
        #st.session_state.bots_response.append(new_variable)  # Store the next bot's response
        time.sleep(5)




if st.button("Chat", key="chatbutton"):
    st.session_state.bots_response = []
    start_beef()


#st.write(":green[Generating...]", )
# Pause button
#if st.button("⏸️", key="pause_button"):  # Pause button with a pause symbol
    #paused = True
    #pass

