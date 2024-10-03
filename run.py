import colorama
import pyfiglet
import random
import time
import sys
import os
from questionlist import mathquestions, geographyquestions
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

# Global Variables
score = 0
player = ""
game = None


# Clearing the terminal
def clean():
    """
    Cleans the terminal.
    """
    os.system("cls" if os.name == "nt" else "clear")


# Displaying a welcome message
def welcome():
    """
    Welcome message, requesting player name.
    """
    global player

    print(
        f"{Fore.GREEN}{Style.BRIGHT}\
            \nWelcome to Quiz Master - Battle of brains!\n"
    )
    time.sleep(1.5)

    # requesting the players name
    validate_player()
    clean()
    print(f"{Fore.CYAN}{Style.BRIGHT}Welcome {player}! Please select a quiz")

    # open the main menu
    menu()


# Validation if user enters a correct name
def validate_player():
    """
    Checking that player enters a valid name.
    """
    global player

    while True:
        player = input(f"{Fore.GREEN}Please enter your name: ")

        if not player.isalpha() or len(player) < 2 or len(player) > 30:
            clean()
            print(
                f"{Fore.RED}{Style.BRIGHT}{player!r} "
                "is not a valid name. Please use only letters"
            )
        else:
            break


# Main menu Rules & Play & Exit
def menu():
    """
    Rules, play, exit
    """
    while True:
        main_menu = int(
            input
            (f"{Fore.YELLOW}{Style.BRIGHT}""[1] Rules \n[2] Play\n[3] Exit\n")
        )
        clean()
        if main_menu == 1:
            # Display Rules
            print(
                f"{Fore.CYAN}{Style.BRIGHT}\
Quizmaster - Battle of brains is a quizgame.\n"
                "You can choose between maths,\n"
                "and geography related questions.\n"
                "For each question, 4 multiple-choice answers are displayed.\n"
                "There is only one correct answer for each question.\n"
                "Each correct answer brings you 10 points.\n"
                "Are you ready to go for the high-score?\n"
                "So choose your favorite quiz and lets go!"
            )
            game_menu()
            break
        elif main_menu == 2:
            # Select quiz
            game_menu()
            break
        elif main_menu == 3:
            # Exit
            print(f"{Fore.GREEN}{Style.BRIGHT}" "Goodbye")
            break
        else:
            print(
                f"{Fore.RED}{Style.BRIGHT}{game!r} "
                "Invalid enter! Please select 1, 2 or 3."
            )


# User selects math or geography quiz
def game_menu():
    """
    Choosing Game-type.
    """
    global game

    while True:
        game_type = int(
            input(f"{Fore.GREEN}{Style.BRIGHT}" "[1] Math \n[2] Geography\n")
        )
        clean()
        if game_type == 1:
            # Math Quiz
            game = mathquestions
            main_math()
            break
        elif game_type == 2:
            # Geography Quiz
            game = geographyquestions
            main_geography()
            break
        else:
            print(
                f"{Fore.RED}{Style.BRIGHT}{game!r} "
                "Invalid enter! Please select 1 or 2."
            )


# Main function / Looping through the mathquestions
def main_math():
    """
    Main function, loops through quiz-questions.
    """
    global score
    # Loop through each question in the list
    for question in mathquestions:
        question_text = question.get("question")
        print(question_text)
        print("--------------")
        print("Choices: ")
        for option in question.get("options"):
            print(option)
        print("--------------")

        while True:
            try:
                user_answer = int(input("Enter answer (number): "))
                correct_answer = int(question.get("answer"))
                if user_answer == correct_answer:
                    clean()
                    print(f"{Fore.GREEN}{correct_answer} is correct! ✅")
                    score += 10
                    print(f"{Fore.GREEN}Your score = {score}")
                else:
                    clean()
                    print(f"{Fore.RED}Wrong ❌, the correct answer is {correct_answer}")
                    print(f"{Fore.RED}Your score = {score}")
                break  # Exit loop if user provided a valid integer answer
            except ValueError:
                # Handle case where the user input isn't a valid integer
                print(f"{Fore.RED}Invalid input. Please enter a valid number for your answer.")


# Main function / Looping through the geographyquestions
def main_geography():
    """
    Main function, loops through questions.
    """
    global score
    # Loop through each question in the list
    for question in geographyquestions:
        question_text = question.get("question")
        print(question_text)
        print("--------------------------------------------------------------")
        print("Choices: ")
        for option in question.get("options"):
            print(option)
        print("--------------------------------------------------------------")
        while True:
            try:
                user_answer = int(input("Enter answer (number): "))
                correct_answer = int(question.get("answer"))
                if user_answer == correct_answer:
                    clean()
                    print(f"{Fore.GREEN}{correct_answer} is correct! ✅")
                    score += 10
                    print(f"{Fore.GREEN}Your score = {score}")
                else:
                    clean()
                    print(f"{Fore.RED}Wrong ❌, the correct answer is {correct_answer}")
                    print(f"{Fore.RED}Your score = {score}")
                break  # Exit loop if user provided a valid integer answer
            except ValueError:
                # Handle case where the user input isn't a valid integer
                print(f"{Fore.RED}Invalid input. Please enter a valid number 1-4 for your answer.")


# Calling functions
clean()
welcome()
