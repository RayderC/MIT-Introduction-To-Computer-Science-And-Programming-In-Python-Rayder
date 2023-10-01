from colorama import Fore

def new_letter_guess(guess, secret_word, guessed_letters, list_secret_word):
    guessed_wrong = []
    guessed_letters.append(guess)  # Adds guessed letter to list of guessed letters
    if guess in list_secret_word:
        list_secret_word.remove(guess)  # If the guessed letter is in the Word it'll remove it from the list
        if not list_secret_word:  # Checks for win
            print(Fore.LIGHTGREEN_EX + "You Win\nThe Word was " + Fore.CYAN + f"{secret_word}")
            input("\nHit enter to exit.")
            exit()
        print(Fore.LIGHTGREEN_EX + f"{guess} is in the word")
    else:
        guessed_wrong.append(guess)
        print(Fore.LIGHTRED_EX + f"{guess} is NOT in the word")