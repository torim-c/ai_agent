import os
from openai import OpenAI
from dotenv import load_dotenv
import argparse



def main():

    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")

    if api_key == None:
        raise RuntimeError ("API Key not found!")



    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    parser = argparse.ArgumentParser(description="user prompt to llm")
    parser.add_argument("user_prompt", type=str, help="User prompt argument after uv run main.py, enclose in double quotes")
    args = parser.parse_args()


    response =  client.chat.completions.create(
    model="openrouter/free",
    messages=[
        {
            "role": "user",
            "content": args.user_prompt,
        }
    ],
)

    if response.usage is None:
        raise RuntimeError("failed API request, usage is None")

    prompt_token_nr = response.usage.prompt_tokens
    response_token_nr = response.usage.completion_tokens

    print(f"Prompt tokens: {prompt_token_nr}")
    print(f"Response tokens: {response_token_nr}")
    print(response.choices[0].message.content)

main()
