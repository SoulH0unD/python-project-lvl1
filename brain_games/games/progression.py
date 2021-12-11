from random import randint


RULES = 'What number is missing in the progression?'


def start():
    list_progression = get_progression()
    index_number = randint(0, 9)
    question = f'Question: {print_progression(list_progression, index_number)}'
    correct_answer = list_progression[index_number]
    return question, str(correct_answer)


def get_progression():
    """Генерация прогрессии"""
    step_progression = randint(2, 6)
    lst_progression = [randint(0, 20)]
    for i in range(9):
        lst_progression.append(lst_progression[i] + step_progression)

    return lst_progression


def print_progression(lst_progression, index_number):
    """Выввод прогресси с пустым элементом"""
    str_progression = ''

    for i in range(10):
        if i != index_number:
            str_progression = str_progression + str(lst_progression[i]) + ' '
        else:
            str_progression = str_progression + '.. '

    return str_progression
