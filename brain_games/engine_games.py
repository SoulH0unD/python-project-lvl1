import brain_games.games.calc as calc
import brain_games.games.even as even
import brain_games.games.gcd as gcd
import brain_games.games.prime as prime
import brain_games.games.progression as progression
import prompt


def games_selection(name_games) -> object:
    """Выбор игры по имени"""
    if name_games == 'calc':
        games = calc.calc
        task = calc.task
    elif name_games == 'even':
        games = even.even
        task = even.task
    elif name_games == 'gcd':
        games = gcd.gcd
        task = gcd.task
    elif name_games == 'prime':
        games = prime.prime
        task = prime.task
    elif name_games == 'progression':
        games = progression.progression
        task = progression.task

    return games, task


def engine(name_games: str):
    count_games = 3
    games = games_selection(name_games)[0]
    print('Welcome to the Brain Games!')
    name_user = prompt.string('May I have your name? ')
    print(f'Hello, {name_user}!')
    print(games_selection(name_games)[1])

    for i in range(count_games):
        answer = games()
        check_the_answer(answer, name_user)

    print(f"Congratulations, {name_user}!")


def check_the_answer(answer, name_user) -> bool:
    """Проверка ответа пользователя"""
    if answer['user'] == answer['correct']:
        print('Correct!')
        return True
    else:
        str1 = f"{answer['user']} is wrong answer ;(."
        str2 = f"Correct answer was {answer['correct']}"
        print(str1, str2)
        print(f"Let's try again, {name_user}!")
        exit()
