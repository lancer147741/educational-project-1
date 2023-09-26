import random


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def main():
    print("brain-gcd")
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print("Hello, " + name)
    print("Find the greatest common divisor of given numbers.")

    num_correct = 0
    num_attempts = 3

    while num_correct < num_attempts:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        correct_answer = gcd(num1, num2)

        print(f"Question: {num1} {num2}")
        user_answer = int(input("Your answer: "))

        if user_answer == correct_answer:
            print("Correct!")
            num_correct += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, '{name}'!")
            break

    if num_correct == num_attempts:
        print(f"Congratulations, {name}")


if __name__ == "__main__":
    main()
