# 🤖 Gemini AI Assistant – Python Terminal Chatbot

A terminal-based chatbot powered by **Google's Gemini Pro** model using the official `google-generativeai` Python SDK.

---

## 🚀 Features

- Interact with Google's `gemini-pro` model via terminal
- Clean and minimal interface
- Auto-retries are handled internally by the SDK
- Environment variables for security

---

## 🧱 Requirements

- Python 3.8+
- A valid [Google AI Studio API Key](https://aistudio.google.com/app/apikey)

---

## 📦 Installation

1. **Clone the repo**:

git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
cd YOUR-REPO-NAME

2.Create a virtual environment (recommended):
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

3.Install dependencies:
pip install google-generativeai python-dotenv

4.Add your API key:
GOOGLE_API_KEY=your_google_api_key_here

==> **Usage**

python main.py
