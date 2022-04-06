import prompt


ROUNDS_COUNT = 3


def play(game):
    """Запуск игры"""
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game.RULES)

    for i in range(ROUNDS_COUNT):
        question, correct_answer = game.get_question_answer()
        print(f'Question: {question}')
        user_response = prompt.string('Your answer: ')

        if user_response == correct_answer:
            print('Correct!')
        else:
            print(f"{user_response} is wrong answer ;(."
                  f"Correct answer was {correct_answer}")
            print(f"Let's try again, {user_name}!")
            exit()

    print(f"Congratulations, {user_name}!")
