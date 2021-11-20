from random import randint


dict_question = {}
dict_variables = {}


def get_text_task():
    return 'What number is missing in the progression?'


def generation_question():
    dict_variables['list_progression'] = get_progression()
    dict_variables['index_number'] = randint(0, 9)
    dict_question['progression'] = print_progression(
        dict_variables['list_progression'],
        dict_variables['index_number'])


def game(answer_user):
    answer = {
        'user': int(answer_user),
        'correct': dict_variables['list_progression']
                                 [dict_variables['index_number']]
    }

    return answer


def get_progression() -> list:
    """Генерация прогрессии"""
    step_progression = randint(2, 6)
    lst_progression = [randint(0, 20)]
    for i in range(9):
        lst_progression.append(lst_progression[i] + step_progression)

    return lst_progression


def print_progression(lst_progression, index_number) -> str:
    """Выввод прогресси с пустым элементом"""
    str_progression = ''

    for i in range(10):
        if i != index_number:
            str_progression = str_progression + str(lst_progression[i]) + ' '
        else:
            str_progression = str_progression + '.. '

    return str_progression
