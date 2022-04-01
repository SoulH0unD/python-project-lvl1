from random import randint


RULES = 'What number is missing in the progression?'


def start_games():
    progression = get_progression()
    index = randint(0, 9)
    question = f'{print_progression(progression, index)}'
    correct_answer = progression[index]
    return question, str(correct_answer)


def get_progression():
    """Генерация прогрессии"""
    step = randint(2, 6)
    progression = [randint(0, 20)]
    for i in range(9):
        progression.append(progression[i] + step)

    return progression


def print_progression(lst_progression, index):
    """Выввод прогресси с пустым элементом"""
    str_progression = ''

    for i in range(10):
        if i != index:
            str_progression = ' '.join([str_progression,
                                        str(lst_progression[i])])
        else:
            str_progression = ' '.join([str_progression, '..'])

    return str_progression.strip()
