# Quizmaster : Battle of brains

# Imports

# Import colorama module
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

# Import pyfiglet module 
import pyfiglet 

# Import random to use random numbers for Quizmaster
import random

import time
import os

# Imports list with all mathquestions from questionlist.py file
from questionlist import mathquestions

# Userscore in the beginning
score = 0

# Looping through the mathquestions
for question in mathquestions:
    question_text = question.get("question")
    print(question_text)
    print("--------------")
    print("Choices: ")
    print(question.get("options"))
    print("--------------")
   
    user_answer = int(input("Enter answer: ")) 
    correct_answer = int(question.get("answer"))

    if user_answer == correct_answer:
        print(f"{Fore.GREEN}Correct! ✅")
        score = score + 10
    else:
        print(f"{Fore.RED}Wrong ❌, the correct answer is {correct_answer}")
    

# Calling functions
start_game = welcome()

print(f"Your score = {score}")