import random
import prompt
from brain_games.function_brain_games import acquaintance_users
from brain_games.function_brain_games import check_the_answer
from brain_games.function_brain_games import isPrime


MAX_NUMBER = 100


def prime():
    name_user = acquaintance_users()
    for i in range(3):
        prime_number = random.randint(2, MAX_NUMBER)
        print('Answer "yes" if given number is prime. Otherwise answer "no".')
        print('Question:', str(prime_number))
        answer_user = prompt.string('Your answer: ')

        check_the_answer(answer_user, isPrime(prime_number), name_user)

    print('Congratulations,', name_user + '!')
