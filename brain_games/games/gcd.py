import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_question():
    number_one = random.randint(1, 50)
    number_two = random.randint(1, 50)
    question = f'{number_one} {number_two}'
    answer = str(get_gcd(number_one, number_two))
    return answer, question


def get_gcd(one, two):
    while two:
        one, two = two, one % two
    return one
