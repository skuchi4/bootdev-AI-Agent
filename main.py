import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
if api_key is None:
    raise RuntimeError("missing API key")

parser = argparse.ArgumentParser(description="accepts coding task, chooses from set of predefined functions")
parser.add_argument("user_prompt", type=str, help="ask the bot something")
args = parser.parse_args()
# Now we can access `args.user_prompt`

def main():
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    messages = [
        {"role": "user", "content": args.user_prompt},
    ]

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
    )
    if response.usage is None:
        raise RuntimeError("failed API request")
    else:
        print(
            f"Prompt tokens: {response.usage.prompt_tokens}\nResponse tokens: {response.usage.completion_tokens}"
        )
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
