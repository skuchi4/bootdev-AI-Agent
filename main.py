import os, json
from dotenv import load_dotenv
from openai import OpenAI
import argparse
from prompts import system_prompt
from call_function import available_functions, call_function

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
if api_key is None:
    raise RuntimeError("missing API key")

parser = argparse.ArgumentParser(description="accepts coding task, chooses from set of predefined functions")
parser.add_argument("user_prompt", type=str, help="ask the bot something")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()
# Now we can access `args.user_prompt`

def main():
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt},
    ]


    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        tools=available_functions,
    )
    if response.usage is None:
        raise RuntimeError("failed API request")
    else:
        if args.verbose:
            print(
                f"User prompt: {args.user_prompt}\nPrompt tokens: {response.usage.prompt_tokens}\nResponse tokens: {response.usage.completion_tokens}"
        )
    message = response.choices[0].message
    if message.tool_calls is None:
        print(response.choices[0].message.content)
    else:
        for tool_call in message.tool_calls:
            function_args = json.loads(tool_call.function.arguments or "{}")
            result_message = call_function(tool_call, args.verbose)
            if result_message["content"] == {}:
                raise Exception("no content")
            if args.verbose:
                print(f"-> {result_message['content']}")



if __name__ == "__main__":
    main()
