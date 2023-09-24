import prompt


def welcome_user():
    uname = prompt.string('May I have your name? ')
    print(f'Hello, {uname}!')

    return uname


uname = welcome_user()

