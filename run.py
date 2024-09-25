# Quizmaster : Battle of brains

# Imports list with all mathquestions from questionlist.py file
from questionlist import mathquestions

# Userscore in the beginning
score = 0

# Looping through the mathquestions
for question in mathquestions:
    question_text = question.get("question")
    print(question_text)
    print("Choices: ")
    print(question.get("options"))

    user_answer = input("Enter answer: ")
    correct_answer = question.get("answer")

    if user_answer == correct_answer:
        score = score + 10
        
print("Your score = ", score)