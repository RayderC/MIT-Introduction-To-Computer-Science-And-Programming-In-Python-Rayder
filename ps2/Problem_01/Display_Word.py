from hangman import secret_word, guessed_letters
from colorama import Fore

def display_word():
    display = Fore.MAGENTA + "Guessed so far: " + Fore.CYAN
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    print(display)