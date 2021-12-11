from random import randint


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def start():
    prime_number = randint(2, 100)
    question = f'Question: {prime_number}'
    if isPrime(prime_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer


def isPrime(number):
    """Проверка числа на простоту"""
    d = 2
    while number % d != 0:
        d += 1
    if d == number:
        return True
    return False
