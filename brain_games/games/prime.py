import random
import prompt


task = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime():
    prime_number = random.randint(2, 100)
    print('Question:', str(prime_number))
    answer_user = prompt.string('Your answer: ')

    answer = {
        'user': answer_user,
        'correct': isPrime(prime_number)
    }

    return answer


def isPrime(n) -> str:
    """Проверка числа на простоту"""
    d = 2
    while n % d != 0:
        d += 1
    if d == n:
        return 'yes'
    return 'no'
