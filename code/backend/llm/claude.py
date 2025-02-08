# calling claude code from: https://cubed.run/blog/how-to-get-started-with-claude-api 

import anthropic

prompt = "how many letter r in strawberry"


client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="", #api key code from https://docs.anthropic.com/en/api/getting-started
)

def claude(prompt):
    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1000,
        # temperature=0.0,
        system="Respond in short and clear sentences.",
        messages=[
        {
        "role": "user",
        "content": prompt
        }
        ]
    )

    return message.content[0].text