from random import randint, choice


RULES = 'What is the result of the expression?'
OPERATORS = ('+', '-', '*')


def start_games():
    number1 = randint(0, 50)
    number2 = randint(0, 50)
    operator = choice(OPERATORS)
    question = f'{number1} {operator} {number2}'
    if operator == '+':
        correct_answer = number1 + number2
    elif operator == '-':
        correct_answer = number1 - number2
    else:
        correct_answer = number1 * number2
    return question, str(correct_answer)
