from langchain_core.messages import HumanMessage
from langchain.tools import Tool
from langchain_google_genai import GoogleGenerativeAI
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
import os

load_dotenv()  # Load .env file for API key

def main():
    model = model = GoogleGenerativeAI(
    model="models/gemini-pro",  # correct format
    temperature=0.0,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)


    tools = []  # Add tools here if needed
    agent_executor = create_react_agent(model, tools)

    print("Hello I am your AI assistant, how can I help you today?")
    print("You can ask me anything, and I can perform calculations for you. Say 'exit' to quit.")

    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        print("\nAssistant: ", end="")
        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=user_input)]}
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="")
        print()

if __name__ == "__main__":
    main()

