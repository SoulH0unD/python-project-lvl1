import random
import prompt
from brain_games.function_brain_games import acquaintance_users, check_the_answer


operator_list = ['+', '-', '*']
MAX_NUMBER = 10


def calc():
    name_user = acquaintance_users()
    for i in range(3):
        number1 = random.randint(0, MAX_NUMBER)
        number2 = random.randint(0, MAX_NUMBER)
        operator = random.choice(operator_list)
        print('Question:', str(number1), operator, str(number2))
        answer_user = prompt.integer('Your answer: ')

        if operator == operator_list[0]:
            correct_answer = number1 + number2
        elif operator == operator_list[1]:
            correct_answer = number1 - number2
        else:
            correct_answer = number1 * number2

        check_the_answer(answer_user, correct_answer, name_user)

    print('Congratulations, ', name_user, '!')
