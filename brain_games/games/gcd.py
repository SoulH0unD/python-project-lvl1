import random
import prompt


task = 'Find the greatest common divisor of given numbers.'


def gcd_euclids(num1, num2) -> int:
    """Алгоритм Евклида для нахождения НОД"""
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 or num2


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
