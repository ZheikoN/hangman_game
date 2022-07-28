import random
from words import words
from graphics import intro, four, three, two, one, over, win

banned_characters = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")


def select_word():
    """
    Randomly selected word from list of words
    """
    selected_word = random.choice(words)
    return selected_word.upper()


def game_logic(word):
    """
    This is the main logic of the game
    """
    print(intro)
    hashed_word = "_" * len(word)
    print("Guessing this word: " + hashed_word)
    used_letter = []
    success_letter = []
    lives = 5
    while lives > 0:
        guessed_letter = input("Guess your letter: \n").upper()
        if guessed_letter in word:
            if guessed_letter in used_letter:
                print("This letter was already used.")
            else:
                print("Success!")
                used_letter.append(guessed_letter)
                success_letter.append(guessed_letter)
                semihashed_word = [letter if letter in success_letter else '_' for letter in word]
                print(' '.join(semihashed_word))
                if '_' not in semihashed_word:
                    print(win)
                    break
        elif guessed_letter not in word:
            if guessed_letter in used_letter:
                print("\nThis letter was already used")
            elif guessed_letter in banned_characters:
                print("Only letters are used!")    
            else:
                lives -= 1
                used_letter.append(guessed_letter)
                if lives == 4:
                    print(four)
                    print(f"You have tried these letters: {used_letter}")
                elif lives == 3:
                    print(three)
                    print(f"You have tried these letters: {used_letter}")
                elif lives == 2:
                    print(two)
                    print(f"You have tried these letters: {used_letter}")
                elif lives == 1:
                    print(one)
                    print(f"You have tried these letters: {used_letter}")
                else:
                    print(over)
                    print(f"Sorry that you hang, the word was '{word}'")
            print(f"\nWrong guess, amount of lives left: {lives}")    
        else:
            print("\nSomething is wrong. Exiting \n")


word = select_word()
game_logic(word)
