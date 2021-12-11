from random import randint

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def start():
    number = randint(1, 50)
    questions = f'Question: {number}'
    if isEven(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return questions, correct_answer


def isEven(number):
    if number % 2 == 0:
        return True
    else:
        return False
