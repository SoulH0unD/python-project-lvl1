from random import randint


RULES = 'What number is missing in the progression?'

START_RANGE_PROGRESSION = 0   # Начальное и конечное значение диапазона
END_RANGE_PROGRESSION = 20    # для выбора 1 элемента прогрессии
START_RANGE_STEP = 2          # Начальное и конечное значение диапазона
END_RANGE_STEP = 9            # для выбора шага прогрессии
START_RANGE_INDEX = 0         # Начальное и конечное значение диапазона
END_RANGE_INDEX = 9           # для выбора индекса скрыытого элемента


def get_question_answer() -> tuple:
    """Возвращаем вопрос и правильный ответ"""
    progression = get_progression()
    empty_index = randint(START_RANGE_INDEX, END_RANGE_INDEX)
    correct_answer = progression[empty_index]
    question = f'{empty_progression(progression, empty_index)}'
    return question, str(correct_answer)


def get_progression() -> list:
    """Генерация прогрессии"""
    step = randint(START_RANGE_STEP, END_RANGE_STEP)
    progression = [randint(START_RANGE_PROGRESSION, END_RANGE_PROGRESSION)]
    for i in range(9):
        progression.append(progression[i] + step)
    return progression


def empty_progression(progression: list, empty_index: int) -> str:
    """Генерация прогресси с пустым элементом"""
    progression[empty_index] = '..'
    return ' '.join(map(str, progression))
