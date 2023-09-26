import prompt

ROUNDS = 0
MAX_WINS = 3  # Максимальное количество выигрышей


def start(game):
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print(game.DESCRIPTION)

    for i in range(ROUNDS):
        right_answer, question = game.get_question()

        print("Question:", question)
        user_answer = prompt.string('Your answer: ')

        if str(user_answer) == str(right_answer):
            print('Correct!')
            MAX_WINS += 1
        else:
            print(
                f"'{user_answer}' is the wrong answer ;(. Correct answer was '{right_answer}'."
                f"\nLet's try again, {name}!")
            return

    print(f"Congratulations, {name}'")
