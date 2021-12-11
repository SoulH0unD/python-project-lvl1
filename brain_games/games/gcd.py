from random import randint

RULES = 'Find the greatest common divisor of given numbers.'


def gcd_euclids(num1, num2) -> int:
    """Алгоритм Евклида для нахождения НОД"""
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 or num2


def start():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    question = f'Question: {number1} {number2}'
    correct_answer = gcd_euclids(number1, number2)

    return question, str(correct_answer)
