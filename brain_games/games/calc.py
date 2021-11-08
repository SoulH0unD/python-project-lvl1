import random
import prompt


task = 'What is the result of the expression?'


def calc():
    operator_list = ['+', '-', '*']
    number1 = random.randint(0, 10)
    number2 = random.randint(0, 10)
    operator = random.choice(operator_list)
    print('Question:', str(number1), operator, str(number2))
    answer_user = prompt.integer('Your answer: ')
    if operator == operator_list[0]:
        correct_answer = number1 + number2
    elif operator == operator_list[1]:
        correct_answer = number1 - number2
    else:
        correct_answer = number1 * number2

    answer = {
        'user': answer_user,
        'correct': correct_answer
    }

    return answer
