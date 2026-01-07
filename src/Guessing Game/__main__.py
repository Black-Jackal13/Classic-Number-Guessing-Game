import random
import time
import hashlib

# Config
MAX_INT = 999
MIN_INT = 0
GUESS_CAP = 5
DIGITS = max(len(str(MAX_INT)), len(str(MIN_INT)))


def generate_random_number():
    raw = random.randint(MIN_INT, MAX_INT)
    padded_num = str(raw).zfill(DIGITS)
    hashed_num = hashlib.sha256(str(raw).encode()).hexdigest()
    return hashed_num


def check_guess(guess, actual):
    padded_guess = str(guess).zfill(DIGITS)
    hashed_guess = hashlib.sha256(str(guess).encode()).hexdigest()

    if hashed_guess == actual:
        return True

    return False


def main():
    actual = generate_random_number()
    guess_count = 0

    print(f"Guess a number between {MIN_INT} and {MAX_INT}")
    print(f"You have {GUESS_CAP} attempts to guess the number")

    while guess_count < GUESS_CAP:
        guess_count += 1
        print("="*40)
        guess = input(f"Guess #{guess_count}:     ")

        print(f"Processing... ")
        time.sleep(1.2)

        if check_guess(guess, actual):
            print("You win! 🎉")
            break
        else:
            print("Incorrect number! Try again if you have more guesses left.")

    else:
        print("\nYou ran out of guesses. Better luck next time! 🔐")


if __name__ == '__main__':
    main()
