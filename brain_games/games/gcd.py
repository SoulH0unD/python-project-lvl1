from random import randint


dict_question = {}


def get_text_task():
    return 'Find the greatest common divisor of given numbers.'


def generation_question():
    dict_question['number1'] = randint(1, 100)
    dict_question['number2'] = randint(1, 100)


def gcd_euclids(num1, num2) -> int:
    """Алгоритм Евклида для нахождения НОД"""
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 or num2


def game(answer_user):
    answer = {
        'user': int(answer_user),
        'correct': gcd_euclids(dict_question['number1'],
                               dict_question['number2'])
    }

    return answer
