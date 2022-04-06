from random import randint

RULES = 'Find the greatest common divisor of given numbers.'
START_RANGE = 1
END_RANGE = 100

def gcd_euclids(num1, num2) -> int:
    """Алгоритм Евклида для нахождения НОД"""
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 or num2


def get_question_answer():
    number1 = randint(START_RANGE, END_RANGE)
    number2 = randint(START_RANGE, END_RANGE)
    question = f'{number1} {number2}'
    correct_answer = gcd_euclids(number1, number2)

    return question, str(correct_answer)
