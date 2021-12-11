from random import randint, choice


RULES = 'What is the result of the expression?'
OPERATOR_LIST = ('+', '-', '*')


def start():
    number1 = randint(0, 50)
    number2 = randint(0, 50)
    operator = choice(OPERATOR_LIST)
    question = f'Question: {number1} {operator} {number2}'
    if operator == OPERATOR_LIST[0]:
        correct_answer = number1 + number2
    elif operator == OPERATOR_LIST[1]:
        correct_answer = number1 - number2
    else:
        correct_answer = number1 * number2
    return question, str(correct_answer)
