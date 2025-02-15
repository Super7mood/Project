# calling claude code from: https://cubed.run/blog/how-to-get-started-with-claude-api 

import anthropic, os
from cmdCall import cmdCall
from prompt import prompts
from dotenv import load_dotenv
load_dotenv()

#Load API keys from enironment variables
apiKey = os.getenv("CLAUDE_API_KEY")

#Error message if api is not found
if apiKey is None:
    raise ValueError("Anthropic API key is not set in environment variables.")

#api key code from https://docs.anthropic.com/en/api/getting-started
client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key = apiKey, 
)

def claude(prompt, responseType="Default"):
    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1000,
        # temperature=0.0,
        system=prompts[responseType], #Instructing the chatbot on how to respond
        messages=[
        {
        "role": "user",
        "content": prompt
        }
        ]
    )

    return message.content[0].text

if __name__ == "__main__":
    print(cmdCall(claude))