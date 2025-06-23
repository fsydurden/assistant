import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("GOOGLE_API_KEY not found in .env file.")
    exit()

# Configure Gemini
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")

print("Hello! I'm your Gemini AI Assistant.")
print("Ask me anything. Type 'exit' to quit.")

while True:
    user_input = input("\nYou: ").strip()
    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    try:
        response = model.generate_content([user_input])
        print("Assistant:", response.text)
    except Exception as e:
        print("Error:", e)
