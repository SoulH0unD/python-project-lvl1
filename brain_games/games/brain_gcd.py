import random
import prompt
from brain_games.function_brain_games import acquaintance_users
from brain_games.function_brain_games import check_the_answer
from brain_games.function_brain_games import gcd_euclids

MAX_NUMBER = 100


def gcd():
    name_user = acquaintance_users()
    for i in range(3):
        number1 = random.randint(1, MAX_NUMBER)
        number2 = random.randint(1, MAX_NUMBER)
        print('Find the greatest common divisor of given numbers.')
        print('Question:', str(number1), str(number2))
        answer_user = prompt.integer('Your answer: ')

        check_the_answer(answer_user, gcd_euclids(number1, number2), name_user)

    print('Congratulations, ', name_user, '!')
