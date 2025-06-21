🤖 AI Chatbot with User Login & Chat History (Streamlit + Gemini 1.5)
This is a full-stack AI chatbot application built with Streamlit and Google's Gemini 1.5 API, featuring:

🔐 User login system using session state

🧠 Gemini 1.5 model integration (Free API key)

💬 Chat UI with user/model bubbles

📦 SQLite database for storing chat history by user

🔐 Environment-safe .env setup for API keys

📁 Project Structure
bash
Copy
Edit
ai-chatbot/
├── pages/
│   └── chatbot.py           # Main chat UI logic
├── login_page.py            # User login & session setup
├── chat_database.py         # SQLite helper functions
├── .env                     # Stores Gemini API key
├── requirements.txt         # Python dependencies
└── README.md
🚀 How to Run
Clone the repo

Create .env file with GEMINI_API_KEY=your-key-here

Run:

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate       # For Windows
pip install -r requirements.txt
streamlit run login_page.py
🧠 Tech Stack
Python, Streamlit

Google Generative AI (Gemini 1.5)

SQLite, dotenv

