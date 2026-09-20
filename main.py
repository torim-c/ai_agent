import os
from openai import OpenAI
from dotenv import load_dotenv
import argparse
from prompts import system_prompt
from call_function import *
import json


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
    parser.add_argument('--verbose', action='store_true', help ="Enable verbose output")
    args = parser.parse_args()


    messages=[
        {
            "role": "system", "content": system_prompt
         },
        {
            "role": "user",
            "content": args.user_prompt,
        },
    ]

    for _ in range(20):
        response =  client.chat.completions.create(
        model="openrouter/free",
        messages= messages,
        tools=available_functions,
        #temperature=0,
        )

        if response.usage is None:
            raise RuntimeError("failed API request, usage is None")

        prompt_token_nr = response.usage.prompt_tokens
        response_token_nr = response.usage.completion_tokens

        if args.verbose:
            print(f"User prompt: {args.user_prompt}")
            print(f"Prompt tokens: {prompt_token_nr}")
            print(f"Response tokens: {response_token_nr}")


        message = response.choices[0].message
        messages.append(message) #keeps previous messages

        if message.tool_calls != None:
            for tool_call in message.tool_calls:
                #function_args = json.loads(tool_call.function.arguments or "{}") now called in call_function.py
                result_message = call_function(tool_call, args.verbose)
                messages.append(result_message)

                if not result_message["content"]:
                    raise Exception("no content in result message")

                if args.verbose == True:
                    print(f"-> {result_message['content']}")
                    
            

                #print(f"Calling function: {tool_call.function.name}{function_args}")
        else:
            print(message.content)
            return  
    print("maximum number of loops (default 20) reached")
    sys.exit(1)

if __name__ == "__main__":
    main()
