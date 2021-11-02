import prompt


def acquaintance_users() -> str:
    """Знакомство с пользователем"""
    print('Welcome to the Brain Games!')
    name_user = prompt.string('May I have your name? ')
    print('Hello, ', name_user, '!')
    return name_user


def check_the_answer(answer_user, correct_answer, name_user) -> bool:
    """Проверка ответа пользователя"""
    if answer_user == correct_answer:
        print('Correct!')
        return True
    else:
        print(answer_user, ' is wrong answer ;(. Correct answer was ',
              correct_answer)
        print('Let`s try again, ', name_user, '!')
        exit()
