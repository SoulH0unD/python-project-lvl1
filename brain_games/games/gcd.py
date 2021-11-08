import random
import prompt
from brain_games.function_brain_games import gcd_euclids


task = 'Find the greatest common divisor of given numbers.'


def gcd():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    print('Question:', str(number1), str(number2))
    answer_user = prompt.integer('Your answer: ')

    answer = {
        'user': answer_user,
        'correct': gcd_euclids(number1, number2)
    }

    return answer
