import random
import prompt
from brain_games.function_brain_games import isPrime


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
