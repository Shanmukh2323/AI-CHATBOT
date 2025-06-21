import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
from chat_database import init_db, save_message, get_all_messages

# Load API key
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if "username" not in st.session_state or "user_id" not in st.session_state:
    st.warning("Please log in first.")
    st.stop()

init_db()
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("models/gemini-1.5-flash")

if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

st.title(f"💬 Ai Chatbot — {st.session_state.username}")

history = get_all_messages(st.session_state.user_id)
for role, msg, time in history:
    with st.chat_message(role):
        st.markdown(f"**{role.capitalize()}** ({time}): {msg}")

user_input = st.chat_input("Ask something...")

if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)
    save_message(st.session_state.user_id, "user", user_input)

    try:
        response = st.session_state.chat.send_message(user_input)
        bot_reply = response.text
    except Exception as e:
        bot_reply = "⚠️ Error from Gemini API"
        st.error(str(e))

    with st.chat_message("model"):
        st.markdown(bot_reply)
    save_message(st.session_state.user_id, "model", bot_reply)
