import random
import prompt

task = 'What number is missing in the progression?'


def progression():
    list_progression = get_progression()
    index_number = random.randint(0, 9)
    print('Question:', print_progression(list_progression, index_number))
    answer_user = prompt.integer('Your answer: ')

    answer = {
        'user': answer_user,
        'correct': list_progression[index_number]
    }

    return answer


def get_progression() -> list:
    """Генерация прогрессии"""
    step_progression = random.randint(2, 6)
    list_progression = [random.randint(0, 20)]

    for i in range(9):
        list_progression.append(list_progression[i] + step_progression)

    return list_progression


def print_progression(list_progression, index_number) -> str:
    """Выввод прогресси с пустым элементом"""
    str_progression = ''

    for i in range(10):
        if i != index_number:
            str_progression = str_progression + str(list_progression[i]) + ' '
        else:
            str_progression = str_progression + '.. '

    return str_progression
