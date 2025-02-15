from chatGPT import chatGPT
from gemini import gemini
from claude import claude
from prompt import prompts
from cmdCall import cmdCall
import time
import threading



def callChatBots(prompt, responseType="Default"):
    s = time.time() # stores the starting time of function calling

    llmFunc = [(chatGPT, "chatGPT"), (gemini, "Gemini"), (claude, "Claude")] # contains the chatbot calling functions and its name

    #code for storing results from threads is from "https://stackoverflow.com/questions/6893968/how-to-get-the-return-value-from-a-thread#:~:text=You%20can%20call%20the%20result,value%20of%20the%20thread's%20function".

    # This function sends a prompt to a chatbot and stores the respond in a dictionary called results
    def chatbot(func, name, prompt, responseType, results):
        start = time.time() # the start time of call the function
        response = func(prompt, responseType) # storing the response of the llm
        end = time.time() # the end time of calling the function
        callTime = end - start # overall time in second in calling the chatbot
        results[name] = (response, round(callTime, 2)) #store the chatbots results in a dictionary 

    threads = [] # stores the threads
    results = {} # stores the results
    for func, name in llmFunc:
        thread = threading.Thread(target=chatbot, args=(func, name, prompt, responseType, results)) #creats a thread of an individual chatbot call
        thread.start() # start running the thread
        threads.append(thread) # storing the thread in an array

    for thread in threads:
        thread.join() # stops the main thread from running until the threads terminates

    
    e = time.time()

    # overallTime = round(e - s, 2) # time taken to get all responses

    # print(f"Overall time: {overallTime}")
    return results


if __name__ == "__main__":
    print(cmdCall(callChatBots))



#Connor's code
# if __name__ == "__main__":
#     print("Enter your question: ")  
#     question = input().strip()  # Ask the user for a question
#     responseType = "None"  # Default response type

#     responseType = responseType if responseType in prompts else "Give a normal response"
#     responses = callChatbots(question, responseType)


#     print("\n\033[1;34m--- AI Responses ---\033[0m")  # Blue Title
#     for model, (response, time_taken) in responses.items():
#         print(f"\033[1;32m{model} ({time_taken}s):\033[0m")  # Green Model Name
#         print(response)
#         print("\n" + "-"*50 + "\n")  # Separator

