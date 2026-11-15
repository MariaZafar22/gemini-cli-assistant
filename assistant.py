"""
Gemini CLI Assistant
Simple Command-Line AI Assistant using the Google Gemini API.

Flow:
user input -> API request -> LLM (Gemini) -> API response -> printed output
"""

import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load GEMINI_API_KEY from the .env file (the key is never written in code)
load_dotenv()

MODEL_NAME = "gemini-3.8-flash"   # change if Google updates the model name
TEMPERATURE = 0.7                 # 0 = focused/predictable, higher = more creative
SYSTEM_INSTRUCTION = (
    "You are a helpful AI assistant. "
    "Give clear, short and accurate answers."
)


def create_client():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY not found. Create a .env file (see .env.example).")
        sys.exit(1)
    return genai.Client(api_key=api_key)


def ask_llm(client, question):
    """Send the user's question to the LLM API and return the text response."""
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=question,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION,
            temperature=TEMPERATURE,
        ),
    )
    return response.text


def main():
    client = create_client()
    print("=== Gemini CLI Assistant (type 'exit' to quit) ===\n")

    while True:
        question = input("You: ").strip()
        if not question:
            continue
        if question.lower() in ("exit", "quit"):
            print("Goodbye!")
            break

        try:
            answer = ask_llm(client, question)
            print(f"\nAI: {answer}\n")
        except Exception as error:
            print(f"\nRequest failed: {error}\n")


if __name__ == "__main__":
    main()
