from random import randint


dict_question = {}


def get_text_task():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generation_question():
    dict_question['prime_number'] = randint(2, 100)


def game(answer_user):
    answer = {
        'user': answer_user,
        'correct': isPrime(dict_question['prime_number'])
    }

    return answer


def isPrime(number) -> str:
    """Проверка числа на простоту"""
    d = 2
    while number % d != 0:
        d += 1
    if d == number:
        return 'yes'
    return 'no'
