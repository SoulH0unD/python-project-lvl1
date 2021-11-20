from random import randint, choice


dict_question = {}


OPERATOR_LIST = ['+', '-', '*']


def get_text_task():
    return 'What is the result of the expression?'


def generation_question():
    dict_question['number1'] = randint(0, 10)
    dict_question['operator'] = choice(OPERATOR_LIST)
    dict_question['number2'] = randint(0, 10)


def game(answer_user):
    if dict_question['operator'] == OPERATOR_LIST[0]:
        correct_answer = dict_question['number1'] + dict_question['number2']
    elif dict_question['operator'] == OPERATOR_LIST[1]:
        correct_answer = dict_question['number1'] - dict_question['number2']
    else:
        correct_answer = dict_question['number1'] * dict_question['number2']
    answer = {
        'user': int(answer_user),
        'correct': correct_answer
    }
    return answer
