import Display_Word
import subprocess
from colorama import Fore


def user_input(amt_of_letters_in_word, secret_word, guessed_letters):
    # Variables for this function
    guessed_wrong = []
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
            guessed_letters.append(guess)  # Adds guessed letter to list of guessed letters
            if guess in list_secret_word:
                list_secret_word.remove(guess)  # If the guessed letter is in the Word it'll remove it from the list
                if not list_secret_word:  # Checks for win
                    print(Fore.LIGHTGREEN_EX + "You Win\nThe Word was " + Fore.CYAN + f"{secret_word}")
                    input("\nHit any key to exit.")
                    exit()
                print(Fore.LIGHTGREEN_EX + f"{guess} is in the word")
            else:
                guessed_wrong.append(guess)
                print(Fore.LIGHTRED_EX + f"{guess} is NOT in the word")
        Display_Word.display_word(secret_word, guessed_letters)
