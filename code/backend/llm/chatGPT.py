# the code to call chatgpt is from https://community.openai.com/t/how-do-i-call-chatgpt-api-with-python-code/554554/2

import requests


# This is function that sends a prompt to the chatgpt chatbot and recieved the answer
def chatGPT(prompt):

    # Api key for chatGPT
    openai_api_key = ""

    #Error message if api is not found
    if openai_api_key is None:
        raise ValueError("OpenAI API key is not set in environment variables.")

    #URL to connect to chatgpt
    url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_api_key}"
    }

    data = {
        "model": "gpt-4o",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    # Check if the request was successful
    if response.status_code == 200:
        # print("Response from OpenAI:", response.json())
        # print('\n')
        return response.json()['choices'][0]['message']['content']
    
    # If it is not successful, return the error message
    print("Error:", response.status_code, response.text)
    return None


