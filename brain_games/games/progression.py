import random


DESCRIPTION = 'What number is missing in the progression?'
LEN_PROGRESSION = 10


def get_question():
    first = random.randint(1, 99)
    step = random.randint(1, 11)
    hidden_position = random.randint(0, LEN_PROGRESSION - 1)
    progression = get_progression(first, step, LEN_PROGRESSION)
    right_answer = progression[hidden_position]
    progression[hidden_position] = '..'
    question = " ".join(progression)
    return right_answer, question


def get_progression(first, step, end):
    progression = []
    for i in range(end):
        progression.append(str(first + step * i))
    return progression
