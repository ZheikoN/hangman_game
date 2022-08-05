import random
from colorama import Fore, Back, Style
from words import words
from graphics import intro, four, three, two, one, over, win


def select_word():
    """
    Randomly selected word from list of words
    """
    selected_word = random.choice(words)
    return selected_word.upper()


def game_logic(word):
    """
    This is the main logic of the game.
    Built on if - statements the game logically
    asses the input and decides what to do with it
    """
    print(Fore.BLUE + intro)
    hashed_word = "_ " * len(word)
    print("Guessing this word: " + hashed_word)
    used_letter = []
    success_letter = []
    lives = 5
    while lives > 0:
        guessed_letter = input(Fore.WHITE + "Guess your letter: \n").upper()
        if guessed_letter in word and len(guessed_letter) == 1 and \
           guessed_letter.isalpha() is True:
            if guessed_letter in used_letter:
                print(Fore.GREEN + "This letter was already used. \n \
                      Used letters:" + "-".join(used_letter) + Style.RESET_ALL)
            else:
                print(Fore.MAGENTA + "Success!" + Style.RESET_ALL)
                used_letter.append(guessed_letter)
                success_letter.append(guessed_letter)
                semihashed_word = [letter if letter in success_letter else '_'
                                   for letter in word]
                print(Fore.BLUE + ' '.join(semihashed_word) + Style.RESET_ALL)
                if '_' not in semihashed_word:
                    print(Fore.YELLOW + win)
                    break
        elif guessed_letter not in word:
            if guessed_letter in used_letter:
                print(Fore.GREEN + "This letter was already used. \n \
                      Used letters:" + "-".join(used_letter) + Style.RESET_ALL)
            elif len(guessed_letter) != 1:
                print("Only single letters please!")
            elif guessed_letter.isalpha() is False:
                print("Only Letters please")
            else:
                lives -= 1
                used_letter.append(guessed_letter)
                msg = Fore.RED + "You have tried these letters: " +\
                                 "-".join(used_letter) + Style.RESET_ALL
                if lives == 4:
                    print(Fore.RED + four)
                    print(msg)
                elif lives == 3:
                    print(Fore.RED + three)
                    print(msg)
                elif lives == 2:
                    print(Fore.RED + two)
                    print(msg)
                elif lives == 1:
                    print(Fore.RED + one)
                    print(msg)
                else:
                    print(Back.RED + over)
                    print(Style.RESET_ALL)
                    print(f"Sorry that you hang, the word was\
                        '{Back.BLUE + word + Style.RESET_ALL}'")
                    break
            print(f"\nWrong guess, amount of lives left: {lives}")
        else:
            print("\nMust be a letter. Try again \n")


word = select_word()
game_logic(word)
