import random


SECRET_NUMBER_SIZE = 3
MAX_TRIES = 10


def generate_secret_number(size: int) -> int:
    """Generate a secret number

    :param size: size of the secret number
    :type size: int
    :return: generated secret number
    :rtype: int
    """
    choices = [str(x) for x in range(0, 10)]
    number = random.sample(choices, size)
    return ''.join(number)


def validate_guess(user_guess: int, secret_random: int) -> tuple[int, int]:
    """Validate if the user entered the right secret number or not.

    :param user_guess: number guessed by the user
    :type user_guess: int
    :param secret_random: secret number to guess
    :type secret_random: int
    :return: number of taureaux and vaches
    :rtype: tuple[int, int]
    """
    taureaux = 0
    vaches = 0

    for index in range(len(user_guess)):
        if user_guess[index] == secret_random[index]:
            taureaux += 1
        elif user_guess[index] in secret_random:
            vaches += 1

    return taureaux, vaches


def is_valid_guess(user_guess: str) -> bool:
    """Check if the number guessed by the user is valid.
    Must be decimal, has the right size and don't have double digits

    :param user_guess: number guessed by the user
    :type user_guess: str
    :return: is a number valid or not
    :rtype: bool
    """
    if not user_guess.isdecimal():
        return True
    user_guess_length = len(user_guess)
    user_guess_set_length = len(set([int(digit) for digit in str(user_guess)]))
    return user_guess_length != SECRET_NUMBER_SIZE or \
        user_guess_set_length != user_guess_length


def play_guessing_game() -> None:
    print("""
- The concept of this game is to guess the secret number chosed by the computer.
- I am thinking of a 3-digit number. Try to guess what it is.
- Here are some clues, when I say:
Vache --> One digit is correct but in the wrong position.
Taureau --> One digit is correct and in the right position.
- I have thought up a number.
- You have 10 guesses to get it.
    \n""")
    while True:
        secret_number = generate_secret_number(SECRET_NUMBER_SIZE)

        tries = 1
        while tries <= MAX_TRIES:
            print(f"Guess #{tries}:")

            user_guess = input("> ")
            while is_valid_guess(user_guess):
                user_guess = input(f"The size of the number must b {SECRET_NUMBER_SIZE}, unique and decimal > ")
            tries += 1

            taureaux, vaches = validate_guess(user_guess, secret_number)
            print(f"{taureaux} taureaux and {vaches} vaches")

            if taureaux == SECRET_NUMBER_SIZE:
                print("""You got it !""")
                break

        if tries > MAX_TRIES:
            print(f"You ran out of guesses. The answer was {secret_number}.")

        repeat = input("Do you want to play again ? (Yes/No)")
        if repeat.lower() in ["no", "n"]:
            break


if __name__ == "__main__":
    play_guessing_game()
