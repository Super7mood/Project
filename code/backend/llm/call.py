from chatGPT import chatGPT
from gemini import gemini
from claude import claude
import time
import threading



prompt = input("Prompt = ") # get the prompt from comand line input
s = time.time() # stores the starting time of function calling

llmFunc = [(chatGPT, "chatGPT"), (gemini, "Gemini"), (claude, "Claude")] # contains the chatbot calling functions and its name

#code for storing results from threads is from "https://stackoverflow.com/questions/6893968/how-to-get-the-return-value-from-a-thread#:~:text=You%20can%20call%20the%20result,value%20of%20the%20thread's%20function".

# This function sends a prompt to a chatbot and stores the respond in a dictionary called results
def chatbot(func, name, prompt, results):
    start = time.time() # the start time of call the function
    result = func(prompt) # 
    print(name, func(prompt))
    end = time.time() # the end time of calling the function
    callTime = end - start # overall time in second in calling the chatbot
    print(f"{name} time: {end - start:2f}")
    results[name] = (result, round(callTime, 2))


threads = [] # stores the threads
results = {} # stores the results
for func, name in llmFunc:
    thread = threading.Thread(target=chatbot, args=(func, name, prompt, results)) #creats a thread of an individual chatbot call
    thread.start() # start running the thread
    threads.append(thread) # storing the thread in an array

for thread in threads:
    thread.join() # stops the main thread from running until the threads terminates

print(results)

e = time.time()

overallTime = round(e - s, 2)

print(f"Overall time: {overallTime}")