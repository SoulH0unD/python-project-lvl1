import random
import prompt
from brain_games.function_brain_games import get_progression
from brain_games.function_brain_games import print_progression


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
