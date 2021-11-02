import prompt
from random import randint


def even():
    print('Welcome to the Brain Games!')
    name_user = prompt.string('May I have your name? ')
    print('Hello,', name_user, '!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        number = randint(1, 50)
        print('Question:', str(number))
        answer_user = prompt.string('Your answer: ')
        if number % 2 == 0:
            parity_check = 'yes'
        else:
            parity_check = 'no'
        if parity_check == answer_user:
            print('Correct!')
        else:
            print("'" + answer_user + "'",
                  "is wrong answer ;(. Correct answer was",
                  "'" + parity_check + "'" + ".")
            print("Let's try again,", name_user + '!')
            break
        if i == 2:
            print('Congratulations,', name_user + '!')
