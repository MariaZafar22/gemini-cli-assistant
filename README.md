# Gemini CLI Assistant

A very small command-line assistant that sends a question to the Google Gemini API and prints the response.

## Files
- `assistant.py` - main program
- `requirements.txt` - Python packages
- `.env.example` - example of the key file (copy to `.env`)
- `.gitignore` - keeps `.env` (your API key) out of GitHub

## Setup
1. Get a free API key from Google AI Studio.
2. Install packages: `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and paste your key:
   `GEMINI_API_KEY=your_real_key`
4. Run: `python assistant.py`

## How the request flows
User types a question in the terminal -> Python program sends it to the Gemini API (with the API key) -> the model generates a response -> the API returns it to the program -> the program prints it on screen.

## Settings used
- `temperature = 0.7` controls how creative or predictable the answer is.
- `system_instruction` tells the model how to behave.

## Security
The API key is stored in `.env` and loaded with `os.getenv`. It is never written in the code and `.env` is excluded from Git.
