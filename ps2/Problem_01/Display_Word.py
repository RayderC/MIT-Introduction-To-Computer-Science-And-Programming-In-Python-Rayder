from colorama import Fore

def display_word(secret_word, guessed_letters):
    display = Fore.MAGENTA + "Guessed so far: " + Fore.CYAN
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    print(display)