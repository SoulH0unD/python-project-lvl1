from random import randint


dict_question = {}


def get_text_task():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def generation_question():
    dict_question['number'] = randint(1, 50)


def game(answer_user):
    answer = {
        'user': "'" + answer_user + "'",
        'correct': isEven(dict_question['number'])
    }

    return answer


def isEven(number):
    if number % 2 == 0:
        return "'yes'"
    else:
        return "'no'"
