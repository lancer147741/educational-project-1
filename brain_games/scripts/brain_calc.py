import random


def welcome_message():
    print('brain-calc\n')
    print('Welcome to the Brain Games!')
    user_name = input('May I have your name? ')
    print(f'Hello, {user_name}!\n')
    return user_name


def generate_question():
    number1 = random.randint(0, 20)
    number2 = random.randint(0, 20)
    operators = ('+', '-', '*')
    operator = random.choice(operators)
    question = f'{number1} {operator} {number2}'
    if operator == '+':
        answer = number1 + number2
    elif operator == '-':
        answer = number1 - number2
    else:
        answer = number1 * number2
    return question, str(answer)


def main():
    user_name = welcome_message()
    correct_answers = 0
    rounds_to_win = 3

    print('What is the result of the expression?')

    while correct_answers < rounds_to_win:
        question, correct_answer = generate_question()
        print(question)
        user_answer = input('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!\n')
            correct_answers += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!\n")
            exit(0)

    print(f'Congratulations, {user_name}!')


if __name__ == "__main__":
    main()
