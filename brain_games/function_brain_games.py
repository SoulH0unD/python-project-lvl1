import prompt
import random


def acquaintance_users() -> str:
    """Знакомство с пользователем"""
    print('Welcome to the Brain Games!')
    name_user = prompt.string('May I have your name? ')
    print('Hello,', name_user + '!')
    return name_user


def check_the_answer(answer_user, correct_answer, name_user) -> bool:
    """Проверка ответа пользователя"""
    if answer_user == correct_answer:
        print('Correct!')
        return True
    else:
        print(answer_user, 'is wrong answer ;(. Correct answer was',
              correct_answer)
        print("Let's try again,", name_user + '!')
        exit()


def gcd_euclids(num1, num2) -> int:
    """Алгоритм Евклида для нахождения НОД"""
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 or num2


def get_progression() -> list:
    """Генерация прогрессии"""
    step_progression = random.randint(2, 6)
    list_progression = [random.randint(0, 20)]

    for i in range(9):
        list_progression.append(list_progression[i] + step_progression)
    return list_progression


def print_progression(list_progression, index_number) -> str:
    """Выввод прогресси с пустым элементом"""
    str_progression = ''

    for i in range(10):
        if i != index_number:
            str_progression = str_progression + str(list_progression[i]) + ' '
        else:
            str_progression = str_progression + '.. '
    return str_progression


def isPrime(n):
    """Проверка числа на простоту"""
    d = 2
    while n % d != 0:
        d += 1
    if d == n:
        return 'yes'
    return 'no'
