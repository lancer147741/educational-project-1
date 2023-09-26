import random


def main():
    print("Welcome to the Prime Number Game!")
    name = input("May I have your name? ")
    print("Hello, " + name + "!")
    print("Answer 'yes' if the number is prime, otherwise answer 'no'.")

    wins = 0

    while wins < 3:
        random_number = random.randint(3, 1223)
        question = random_number
        right_answer = 'yes' if is_prime(random_number) else 'no'

        print("Question:", question)
        user_answer = input("Your answer (yes/no): ")

        if user_answer == right_answer:
            print("Correct!")
            wins += 1
        else:
            print(
                f"Sorry, '{user_answer}' is the wrong answer ;(. Correct answer was '{right_answer}'.")
            print("Game over, " + name + "! You won", wins, "times.")
            break

    print(f"Congratulations, {name}! You won {wins} times!")


def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True


if __name__ == "__main__":
    main()
