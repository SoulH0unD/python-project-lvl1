from random import randint


RULES = 'What number is missing in the progression?'

#Указываем начальные и конечное значение диапазона
#из которого выбирается первый элемент прогрессии
START_RANGE_PROGRESSION = 0
END_RANGE_PROGRESSION = 20

#Указываем начальные и конечное значение диапазона
#из которого выбирается шаг прогрессии
START_RANGE_STEP = 2
END_RANGE_STEP = 9

#Указываем начальные и конечное значение диапазона 
#из которого будет выбираться индекс элемента который будет скрыт
START_RANGE_INDEX = 0
END_RANGE_INDEX = 9


def get_question_answer():
    progression = get_progression()
    empty_index = randint(START_RANGE_INDEX, END_RANGE_INDEX)
    correct_answer = progression[empty_index]
    question = f'{empty_progression(progression, empty_index)}'
    return question, str(correct_answer)


def get_progression():
    """Генерация прогрессии"""
    step = randint(START_RANGE_STEP, END_RANGE_STEP)
    progression = [randint(START_RANGE_PROGRESSION, END_RANGE_PROGRESSION)]
    for i in range(9):
        progression.append(progression[i] + step)
    return progression


def empty_progression(progression, empty_index):
    """Генерация прогресси с пустым элементом"""
    progression[empty_index] = '..'
    return ' '.join(map(str, progression))
