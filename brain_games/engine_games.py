import brain_games.games.calc as calc
import brain_games.games.even as even
import brain_games.games.gcd as gcd
import brain_games.games.prime as prime
import brain_games.games.progression as progression
from brain_games.function_brain_games import acquaintance_users
from brain_games.function_brain_games import check_the_answer


def games_selection(name_games) -> object:
    """Выбор игры по имени"""
    if name_games == 'calc':
        games = calc.calc
    elif name_games == 'even':
        games = even.even
    elif name_games == 'gcd':
        games = gcd.gcd
    elif name_games == 'prime':
        games = prime.prime
    elif name_games == 'progression':
        games = progression.progression

    return games


def task_selection(name_games) -> str:
    """Выбор задания по имени"""
    if name_games == 'calc':
        task = calc.task
    elif name_games == 'even':
        task = even.task
    elif name_games == 'gcd':
        task = gcd.task
    elif name_games == 'prime':
        task = prime.task
    elif name_games == 'progression':
        task = progression.task

    return task


def engine(name_games: str):
    count_games = 3
    games = games_selection(name_games)
    name_user = acquaintance_users()
    print(task_selection(name_games))

    for i in range(count_games):
        answer = games()
        check_the_answer(answer, name_user)

    print(f"Congratulations, {name_user}!")
