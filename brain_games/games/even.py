from random import randint

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def start_games():
    number = randint(1, 50)
    questions = f'{number}'
    if is_even(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return questions, correct_answer


def is_even(number):
    return number % 2 == 0
