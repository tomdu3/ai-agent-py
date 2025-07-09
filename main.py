import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if len(sys.argv) < 2:
    print('Error: Argument missing: uv run main.py "here goes the prompt"')
    sys.exit(1)

user_prompt = sys.argv[1]
messages = [
    types.Content(
        role="user", 
        parts=[
            types.Part(text=user_prompt)
            ]
        ),
]

client = genai.Client(api_key=api_key)

def main():
    res = client.models.generate_content(
            model='gemini-2.0-flash-001',
            contents=messages,
            )
    print(res.text)
    if len(sys.argv) > 2:
        if sys.argv[2] == '--verbose':
            
            usage_meta = res.usage_metadata
            print(f'User prompt: {user_prompt}')
            print(f'Prompt tokens: {usage_meta.prompt_token_count}')
            print(f'Response tokens: {usage_meta.candidates_token_count}')
if __name__ == "__main__":
    main()
