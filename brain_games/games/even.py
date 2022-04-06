from random import randint

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
START_RANGE = 1
END_RANGE = 50

def get_question_answer():
    number = randint(START_RANGE, END_RANGE)
    question = f'{number}'
    if is_even(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer


def is_even(number):
    return number % 2 == 0
