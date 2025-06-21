import streamlit as st
from chat_database import init_db, get_user_id

init_db()

st.title("🔐 Gemini Chatbot Login")

username = st.text_input("Enter your username")

if username:
    if st.button("Login"):
        user_id = get_user_id(username)
        st.session_state.username = username
        st.session_state.user_id = user_id
        st.success(f"Welcome, {username}!")

        st.switch_page("pages/streamlit_chatbot.py")
