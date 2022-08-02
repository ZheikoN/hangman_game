import random
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
    print(intro)
    hashed_word = "_" * len(word)
    print("Guessing this word: " + hashed_word)
    used_letter = []
    success_letter = []
    lives = 5
    while lives > 0:
        guessed_letter = input("Guess your letter: \n").upper()
        if guessed_letter in word and len(guessed_letter) == 1 and \
           guessed_letter.isalpha() is True:
            if guessed_letter in used_letter:
                print("This letter was already used. \nUsed letters: " +
                      "-".join(used_letter))
            else:
                print("Success!")
                used_letter.append(guessed_letter)
                success_letter.append(guessed_letter)
                semihashed_word = [letter if letter in success_letter else '_'
                                   for letter in word]
                print(' '.join(semihashed_word))
                if '_' not in semihashed_word:
                    print(win)
                    break
        elif guessed_letter not in word:
            if guessed_letter in used_letter:
                print("\nThis letter was already used. \nUsed letters: " +
                      "-".join(used_letter))
            elif len(guessed_letter) != 1:
                print("Only single letters please!")
            elif guessed_letter.isalpha() is False:
                print("Only Letters please")
            else:
                lives -= 1
                used_letter.append(guessed_letter)
                msg = "You have tried these letters: " + "-".join(used_letter)
                if lives == 4:
                    print(four)
                    print(msg)
                elif lives == 3:
                    print(three)
                    print(msg)
                elif lives == 2:
                    print(two)
                    print(msg)
                elif lives == 1:
                    print(one)
                    print(msg)
                else:
                    print(over)
                    print(f"Sorry that you hang, the word was '{word}'")
                    break
            print(f"\nWrong guess, amount of lives left: {lives}")
        else:
            print("\nMust be a letter. Try again \n")


word = select_word()
game_logic(word)
