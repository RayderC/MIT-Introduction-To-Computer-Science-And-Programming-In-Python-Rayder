import Display_Word
import subprocess
from colorama import Fore
import new_letter


def user_input(amt_of_letters_in_word, secret_word, guessed_letters):
    # Variables for this function

    list_secret_word = list(set(secret_word))

    while True:
        # Print Reset colors and tells you how many letters are in the word you're guessing and get your input.
        print(Fore.RESET)
        print(
            Fore.LIGHTMAGENTA_EX + "\nThe word you're guessing has " + Fore.CYAN + f"{amt_of_letters_in_word} " + Fore.LIGHTMAGENTA_EX + "letters in it.")
        guess = input(Fore.LIGHTYELLOW_EX + "Enter a letter to guess: ").lower()
        # Clears Shell
        subprocess.run('cls', shell=True)
        # Checks if guess is a Valid input
        if len(guess) != 1 or not guess.isalpha():
            print(Fore.RED + "Please enter a valid single letter.")
            Display_Word.display_word(secret_word, guessed_letters)
            continue

        # Checks if letter was already guessed
        if guess in guessed_letters:
            print(Fore.RED + f"You've already guessed {guess}, please try a new letter.")

        else:
            new_letter.new_letter_guess(guess, secret_word, guessed_letters, list_secret_word)
        Display_Word.display_word(secret_word, guessed_letters)
