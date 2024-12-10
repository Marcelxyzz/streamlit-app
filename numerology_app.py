import streamlit as st
from calculate_numbers import calculate_life_path_number
from calculate_numbers import calculate_destiny_number
from hugging_chat_connection import generate_response
from calculate_numbers import calculate_personality_number
from calculate_numbers import calculate_soul_number

st.set_page_config(page_title="NumerologyGPT",
                   page_icon="💻")

st.image(
    image="https://images.squarespace-cdn.com/content/v1/51d45e1ce4b0ed5a1e73808b/1564633957565-NX8AD32YBHLHHIMAUE6Y/numerology-banner%402x.jpg?format=2500w")
st.title("NumerologyGPT")

if "lifepath_count" not in st.session_state:
    st.session_state.lifepath_count = 0

if "destiny_count" not in st.session_state:
    st.session_state.destiny_count = 0

if "personality_count" not in st.session_state:
    st.session_state.personality_count = 0

if "soul_count" not in st.session_state:
    st.session_state.soul_count = 0


def activate_lifepath():
    st.session_state.lifepath_count = 1
    st.session_state.destiny_count = 0
    st.session_state.personality_count = 0
    st.session_state.soul_count = 0


def activate_destiny():
    st.session_state.destiny_count = 1
    st.session_state.lifepath_count = 0
    st.session_state.personality_count = 0
    st.session_state.soul_count = 0


def activate_personality():
    st.session_state.personality_count = 1
    st.session_state.destiny_count = 0
    st.session_state.lifepath_count = 0
    st.session_state.soul_count = 0


def activate_soul():
    st.session_state.soul_count = 1
    st.session_state.personality_count = 0
    st.session_state.destiny_count = 0
    st.session_state.lifepath_count = 0


with st.chat_message("assistant"):
    st.write("Hello Human! What would you like me to calculate?")
    c1, c2 = st.columns(2)
    with c1:
        life_path = st.button("Life Path Number", on_click=activate_lifepath)
        personality = st.button("Personality Number", on_click=activate_personality)
    with c2:
        destiny = st.button("Destiny Number", on_click=activate_destiny)
        soul = st.button("Soul Number", on_click=activate_soul)

if st.session_state.lifepath_count == 1:
    with st.chat_message("assistant"):
        dob = st.date_input("What is your date of birth?", value=None)
        if dob:
            life_path_number = calculate_life_path_number(dob)
            st.write(f"Your life path number is {life_path_number}!")
            prompt = st.chat_input("Enter prompt")
            if prompt:
                with st.spinner("Thinking"):
                    result = generate_response(prompt)
                    st.write(result)

if st.session_state.destiny_count == 1:
    with st.chat_message("assistant"):
        name = st.text_input("What is your full name?")
        if name:
            destiny_number = calculate_destiny_number(name)
            st.write(f"Your destiny number is {destiny_number}!")
            prompt = st.chat_input("Enter prompt")
            if prompt:
                with st.spinner("Thinking"):
                    result = generate_response(prompt)
                    st.write(result)

if st.session_state.personality_count == 1:
    with st.chat_message("assistant"):
        name = st.text_input("What is your full name?")
        if name:
            personality_number = calculate_personality_number(name)
            st.write(f"Your personality number is {personality_number}!")
            prompt = st.chat_input("Enter prompt")
            if prompt:
                with st.spinner("Thinking"):
                    result = generate_response(prompt)
                    st.write(result)

if st.session_state.soul_count == 1:
    with st.chat_message("assistant"):
        name = st.text_input("What is your full name?")
        if name:
            soul_number = calculate_soul_number(name)
            st.write(f"Your soul number is {soul_number}!")
            prompt = st.chat_input("Enter prompt")
            if prompt:
                with st.spinner("Thinking"):
                    result = generate_response(prompt)
                    st.write(result)
