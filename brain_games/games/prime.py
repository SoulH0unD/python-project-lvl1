from random import randint


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
START_RANGE = 2
END_RANGE = 100


def get_question_answer() -> tuple:
    """Возвращаем вопрос и правильный ответ"""
    prime_number = randint(START_RANGE, END_RANGE)
    question = f'{prime_number}'
    if is_prime(prime_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer


def is_prime(number) -> bool:
    """Проверка числа на простоту"""
    d = 2
    while number % d != 0:
        d += 1
    if d == number:
        return True
    return False
