import pandas as pd # used to read, write to csvs and converting data to a dataframe
import numpy as np


data = pd.read_csv("../unprocessed/puzzle.csv") # storing the content of the csv in data


question = np.array(data.pop("Problem")) # Storing the questions
options = np.array(data.pop("options")) # Storing the multiple choice option strings
correct = np.array(data.pop("correct")) # Storing the answers to the multiple choice quesitons

# This function extracts the number from the string
def processOption(s):
    start = None
    end = None
    i = 0
    while i < len(s):
        if s[i].isdigit():
            if not start:
                start = i
                end = i
            else:
                end = i
        i += 1
    if start and end:
        return s[start: end+1]
    return "None"

# This function checks if the certain characters are in a string or not
def isNotIn(chars, string):
    for c in chars:
        if c in string:
            return False
    return True

dataStructure = {"Question": [], "Answer": [], "Options": [], "Correct": []} #Creating a data strcuture for the final csv  

puzzle = pd.DataFrame(dataStructure)

choiceIndex = {"a" : 0, "b": 1, "c":2, "d":3, "e":4} # assiging letters to their relevent index in the multiple choice
totalNot = 0 #Tracks the number of rows answers that are formated in a non number format
i = 0

#This while loop iterate through the first 3000 content of the data
while i < 3000:
    option = options[i].split(",") #split the multiple choice string into a list with each individual option alone
    optionString = option[choiceIndex[correct[i]]] # getting the correct answer
    optionNum = processOption(optionString) # trimming the correct answer to just a number

    # If it is correct number is not in the formate of an integer or float then it will be ignored
    if not(not optionNum.isdigit() and optionNum.find(".") == -1) and isNotIn("−-%", optionString) and optionNum.find("cm") == -1:
        puzzle.loc[len(puzzle)] = [question[i], optionNum, options[i], correct[i]] # Adding row to the data frame

        totalNot += 1
    
    i += 1

puzzle[:500].to_csv("../processed/number/puzzleScore.csv") # storing the data that will be used for accuracy score
puzzle[500:1000].to_csv("../processed/number/puzzleEvaluation.csv") # storing the data that will be used for evaluation