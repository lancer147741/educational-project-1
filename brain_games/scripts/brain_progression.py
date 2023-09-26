import random


def main():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print("Hello, " + name + "!")
    print("What number is missing in the progression?")

    progression_length = 10
    wins = 0

    while wins < 3:
        start = random.randint(1, 99)
        step = random.randint(1, 11)
        hidden_position = random.randint(0, progression_length - 1)
        progression = []

        for i in range(progression_length):
            current_value = start + step * i
            if i == hidden_position:
                right_answer = current_value
                progression.append('..')
            else:
                progression.append(str(current_value))

        question = " ".join(progression)
        print("Question:", question)

        user_answer = input("Your answer: ")

        if user_answer.isdigit():
            user_answer = int(user_answer)
            if user_answer == right_answer:
                print("Correct!")
                wins += 1
            else:
                print(
                    f"'{user_answer}' is the wrong answer ;(. Correct answer was '{right_answer}'.")
                print(f"Let's try again, '{name}'!")
                break
        else:
            print("Please enter a valid number.")

    if wins == 3:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
