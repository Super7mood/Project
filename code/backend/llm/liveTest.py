from call import callChatbots

prompt = input("Prompt = ") # get the prompt from comand line input

inputStr = "Pick the response Type:\n1: Default\n2: Number\nChoice="
option = int(input(inputStr))

while option < 1 or option > 2:
    option = int(input(inputStr))

responseType = {1: "None", 2: "Number"}

responses = callChatbots(prompt, responseType[option])

print(responses)