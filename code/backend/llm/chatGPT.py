# the code to call chatgpt is from https://community.openai.com/t/how-do-i-call-chatgpt-api-with-python-code/554554/2

import os, sys, requests
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import requests
from cmdCall import cmdCall
from prompt import prompts
from dotenv import load_dotenv
load_dotenv()

# This is function that sends a prompt to the chatgpt chatbot and recieved the answer
def chatGPT(prompt, responseType="Default"):

    
    #Load API keys from enironment variables
    apiKey = os.getenv("CHATGPT_API_KEY")
    #Error message if api is not found
    if apiKey is None:
        raise ValueError("OpenAI API key is not set in environment variables.")

    #URL to connect to chatgpt
    url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {apiKey}"
    }

    data = {
        "model": "gpt-4o",
        "messages": [
            {
                "role": "system",
                "content": prompts[responseType]
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

if __name__ == "__main__":
    print(cmdCall(chatGPT))