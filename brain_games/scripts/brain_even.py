from random import randint


def call():
    print('Welcome to the Brain Games!')
    YourName = input('May I have your name? ')
    print('Hello, ' + YourName + '!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answers = 0

    while correct_answers < 3:
        number = randint(1, 9999999)
        print("Question: " + str(number))
        join = input("Your answer: ")

        if number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        if correct_answer == join.lower():
            correct_answers += 1
            print('Correct!')
        else:
            print(
                "'" + join + "' is the wrong answer ;(. Correct answer was '" + correct_answer + "'.")
            print("Let's try again, " + YourName + "!")
            break

    if correct_answers == 3:
        print('Congratulations, ' + YourName + '!')


if __name__ == "__main__":
    main()
