import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")


client = genai.Client(api_key=api_key)

def main():
    res = client.models.generate_content(
            model='gemini-2.0-flash-001',
            contents='Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.'
            )
    print(res.text)
    usage_meta = res.usage_metadata
    print(f'Prompt tokens: {usage_meta.prompt_token_count}')
    print(f'Response tokens: {usage_meta.candidates_token_count}')
if __name__ == "__main__":
    main()
