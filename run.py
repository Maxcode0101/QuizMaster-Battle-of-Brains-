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
import sys, os

# Imports list with questions from questionlist.py file
from questionlist import mathquestions
from questionlist import geographyquestions


# Global Variables

# Userscore in the beginning
SCORE = 0

PLAYER = ""
GAME = None

def clean():
    """
    Cleans the terminal.
    """
    os.system("cls" if os.name == "nt" else "clear")

def welcome():
    """
    Welcome message, requesting player name.
    """
    global PLAYER

    print(f"{Fore.GREEN}{Style.BRIGHT} \nWelcome to Quiz Master - Battle of brains!\n")
    time.sleep(1.5)

    # requesting the players name
    validate_player()
    clean()
    print(f"{Fore.CYAN}{Style.BRIGHT}Welcome {PLAYER}! Please select a quiz")

    # open the main menu
    menu()


def validate_player():
    """
    Checking that player enters a valid name.
    """
    global PLAYER

    while True:
        PLAYER = input(f"{Fore.GREEN}Please enter your name: ")

        if not PLAYER.isalpha() or len(PLAYER) < 2 or len(PLAYER) > 30:
            clean()
            print(
                f"{Fore.RED}{Style.BRIGHT}{PLAYER!r} "
                "is not a valid name. Please use only letters")
        else:
            break

def menu():
    """
    Rules, play, exit
    """
    while True:
        main_menu = int(input(f"{Fore.GREEN}{Style.BRIGHT}""[1] Rules \n[2] Play\n [3] Exit\n"))
        clean()
        if main_menu == 1:
                # Display Rules
                print(f"{Fore.GREEN}{Style.BRIGHT}""Quizmaster - Battle of brains is a quizgame. You can choose between maths and geography related questions. For each question 4 multiplychoice answers getting displayed. There is only one correct answer. Each correct answer brings you 10 points. Are you ready to go for the high-score? So choose your favorite quiz and lets go!")
                game_menu()
                break
        elif main_menu == 2:
                # Select quiz
                game_menu()
                break
        elif main_menu ==3:
                # Exit
                print(f"{Fore.GREEN}{Style.BRIGHT}""Goodbye")
                break
        else:
                print(
                    f"{Fore.RED}{Style.BRIGHT}{game!r} "
                    "Invalid enter! Please select 1, 2 or 3.")



def game_menu():
    """
    Choosing Game-type.
    """
    global GAME


    while True:
        game_type = int(input(f"{Fore.GREEN}{Style.BRIGHT}""[1] Math \n[2] Geography\n"))
        clean()
        if game_type == 1:
                # Math Quiz
                GAME = mathquestions
                main_math()
                break
        elif game_type == 2:
                # Geography Quiz
                GAME = geographyquestions
                main_geography()
                break
        else:
                print(
                    f"{Fore.RED}{Style.BRIGHT}{game!r} "
                    "Invalid enter! Please select 1 or 2.")


# Looping through the mathquestions
def main_math():
    """
    Main function, loops through quiz-questions.
    """
    global SCORE
    # Loop
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
            print(f"{Fore.GREEN}{correct_answer} is correct! ✅")
            print(f"{Fore.GREEN}Your score = {SCORE+10}")
        else:
            print(f"{Fore.RED}Wrong ❌, the correct answer is {correct_answer}")
            print(f"{Fore.RED}Your score = {SCORE}")
        

# Looping through the geographyquestions
def main_geography():
    """
    Main function, loops through questions.
    """
    global SCORE
    # Loop
    for question in geographyquestions:
        question_text = question.get("question")
        print(question_text)
        print("--------------")
        print("Choices: ")
        print(question.get("options"))
        print("--------------")
    
        user_answer = int(input("Enter answer: "))
        correct_answer = int(question.get("answer"))

        if user_answer == correct_answer:
            print(f"{Fore.GREEN}{correct_answer} is correct! ✅")
            print(f"{Fore.GREEN}Your score = {SCORE+10}")
        else:
            print(f"{Fore.RED}Wrong ❌, the correct answer is {correct_answer}")
            print(f"{Fore.RED}Your score = {SCORE}")
        
        clean()

# Calling functions
clean()
welcome()
