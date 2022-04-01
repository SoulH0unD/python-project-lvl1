import prompt


ROUNDS_COUNT = 3


def begin(game):
    print('Welcome to the Brain Games!')
    name_user = prompt.string('May I have your name? ')
    print(f'Hello, {name_user}!')
    print(game.RULES)

    for i in range(ROUNDS_COUNT):
        question, correct_answer = game.start_games()
        print(f'Question: {question}')
        user_response = prompt.string('Your answer: ')

        if user_response == correct_answer:
            print('Correct!')
        else:
            str1 = f"{user_response} is wrong answer ;(."
            str2 = f"Correct answer was {correct_answer}"
            print(str1, str2)
            print(f"Let's try again, {name_user}!")
            exit()

    print(f"Congratulations, {name_user}!")
