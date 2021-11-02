import random
import prompt
from brain_games.function_brain_games import acquaintance_users
from brain_games.function_brain_games import check_the_answer
from brain_games.function_brain_games import get_progression
from brain_games.function_brain_games import print_progression

MAX_NUMBER = 100


def progression():
    name_user = acquaintance_users()
    for i in range(3):
        list_progression = get_progression()
        index_number = random.randint(0, 9)
        print('What number is missing in the progression?')
        print('Question:', print_progression(list_progression, index_number))
        answer_user = prompt.integer('Your answer: ')

        check_the_answer(answer_user, list_progression[index_number], name_user)

    print('Congratulations, ', name_user, '!')
