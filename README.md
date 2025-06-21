# AI-CHATBOT
# 🤖 AI Chatbot – Streamlit App with User Login and Chat History

This project is a full-stack AI chatbot built using **Google Gemini 1.5 API** and **Streamlit**, designed with a clean UI, persistent user login, and chat history storage via **SQLite**.

---

## 🚀 Features

- 🔐 **User Login System** — Each user has their own chat history.
- 💬 **Conversational Chat Interface** — With user/model chat bubbles.
- 🧠 **Gemini 1.5 API Integration** — Leverages the free tier of Google’s GenAI models.
- 💾 **Chat History Storage** — Messages saved in a local SQLite database per user.
- 🔐 **Secure API Key Handling** — Uses `.env` for safe environment variable access.

---

## 📁 Project Structure

ai-chatbot/
├── pages/
│   └── chatbot.py           # Main chat UI logic
├── login_page.py            # User login & session setup
├── chat_database.py         # SQLite helper functions
├── .env                     # Stores Gemini API key
├── requirements.txt         # Python dependencies
└── README.md

## ⚙️ Getting Started

### 1. Clone the Repository

git clone https://github.com/your-username/ai-chatbot.git
cd ai-chatbot
2. Create and Activate Virtual Environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate       # On Windows
# source venv/bin/activate  # On Mac/Linux
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Add Your Gemini API Key
Create a .env file and add your Google API key:

ini
Copy
Edit
GEMINI_API_KEY=your-api-key-here
You can get a free Gemini API key from: https://makersuite.google.com/app/apikey

5. Run the App
bash
Copy
Edit
streamlit run login_page.py
🧠 Tech Stack
Frontend: Streamlit

Backend: Python

LLM API: Gemini 1.5 (via google.generativeai)

Database: SQLite

Security: python-dotenv for secrets


📌 To Do
 Add password encryption and user signup

📄 License
This project is licensed under the MIT License.
