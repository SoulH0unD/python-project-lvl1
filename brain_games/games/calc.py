from random import randint, choice


RULES = 'What is the result of the expression?'
OPERATORS = ('+', '-', '*')
START_RANGE = 0
END_RANGE = 50

def get_question_answer():
    number1 = randint(START_RANGE, END_RANGE)
    number2 = randint(START_RANGE, END_RANGE)
    operator = choice(OPERATORS)
    question = f'{number1} {operator} {number2}'
    if operator == '+':
        correct_answer = number1 + number2
    elif operator == '-':
        correct_answer = number1 - number2
    else:
        correct_answer = number1 * number2
    return question, str(correct_answer)
