import prompt


COUNT_GAMES = 3


def engine(game):
    print('Welcome to the Brain Games!')
    name_user = prompt.string('May I have your name? ')
    print(f'Hello, {name_user}!')
    print(game.get_text_task())

    for i in range(COUNT_GAMES):
        game.generation_question()
        print(
            'Question:',
            " ".join([str(i) for i in game.dict_question.values()]))
        answer_user = prompt.string('Your answer: ')
        answer = game.game(answer_user)
        if answer['user'] == answer['correct']:
            print('Correct!')
        else:
            str1 = f"{answer['user']} is wrong answer ;(."
            str2 = f"Correct answer was {answer['correct']}"
            print(str1, str2)
            print(f"Let's try again, {name_user}!")
            exit()

    print(f"Congratulations, {name_user}!")
