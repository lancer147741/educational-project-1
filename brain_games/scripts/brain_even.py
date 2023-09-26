from random import randint


def main():
    print('Welcome to the Brain Games!')
    your_name = input('May I have your name? ')
    print('Hello, ' + your_name + '!')
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
            print("Let's try again, " + your_name + "!")
            break

    if correct_answers == 3:
        print('Congratulations, ' + your_name + '!')


if __name__ == "__main__":
    main()
