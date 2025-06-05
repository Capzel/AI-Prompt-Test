import openai
import os
from dotenv import load_dotenv
import re

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

def sanitize_filename(text):
    return re.sub(r'[^a-zA-Z0-9_]', '_', text.strip().lower())

def ask_chatgpt(prompt, temperature, top_p):
    client = openai.OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an assistant."},
            {"role": "user", "content": prompt + "Dont add any explanation or comments. Only code!"}
        ],
        temperature=temperature,
        top_p=top_p,
        max_tokens=600,
    )
    return response.choices[0].message.content

def save_response_as_file(code, filename):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(code)

if __name__ == "__main__":
     #user_prompt = input("Ask ChatGPT: ")
    user_prompt = "make me tic tac toe in pyhton"

    filename_base = sanitize_filename(user_prompt[:30])

    settings = [
        (1.2, 0.9), #settings 1
        (0.2, 0.2), #settings 2
        (1.2, 0.2), #settings 3
        (0.2, 0.9), #settings 4
        (0.7, 0.2), #settings 5
        (0.7, 0.9), #settings 6
        (0.2, 0.5), #settings 7
        (1.2, 0.5), #settings 8
        (0.7, 0.5)  #settings 9
    ]

    for idx, (temp, top_p) in enumerate(settings, 1):
        print(f"Requesting setting {idx} (temperature={temp}, top_p={top_p})...")
        result = ask_chatgpt(user_prompt, temp, top_p)
        filename = f"{filename_base}_setting_{idx}.py"
        save_response_as_file(result, filename)
        print(f"Saved: {filename}")
