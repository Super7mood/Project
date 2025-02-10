# calling claude code from: https://cubed.run/blog/how-to-get-started-with-claude-api 

import anthropic

prompt = "how many letter r in strawberry"


client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="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", #api key code from https://docs.anthropic.com/en/api/getting-started
)

def claude(prompt, responseType="Give a normal response"):
    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1000,
        # temperature=0.0,
        system=responseType, #Instructing the chatbot on how to respond
        messages=[
        {
        "role": "user",
        "content": prompt
        }
        ]
    )

    return message.content[0].text