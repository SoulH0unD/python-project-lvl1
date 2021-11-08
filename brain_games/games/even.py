import prompt
from random import randint


task = 'Answer "yes" if the number is even, otherwise answer "no".'


def even():
    number = randint(1, 50)
    print('Question:', str(number))
    answer_user = "'" + prompt.string('Your answer: ') + "'"
    if number % 2 == 0:
        correct_answer = "'yes'"
    else:
        correct_answer = "'no'"

    answer = {
        'user': answer_user,
        'correct': correct_answer
    }

    return answer
