import random

words = ("apple", "banana", "cherry")
banned_characters = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")
intro = """
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
"""
win = """
             ___________
            '._==_==_=_.'
            .-\:      /-.
           | (|:.     |) |
            '-|:.     |-'
              \::.    /
               '::. .'
                 ) (
               _.' '._
Here is your trophy for beating the game!
"""



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
        guessed_letter = input("guess your letter\n").upper()
        if guessed_letter in word:
            if guessed_letter in used_letter:
                print("this letter was already used")
            # elif guessed_letter not in word:
            #     print(f"wrong guess, amount of lives left:{lives - 1}")
            #     lives -= 1
            #     used_letter.append(guessed_letter)
            elif guessed_letter in banned_characters:
                print("no numbers please")
            else:
                print("success!")
                used_letter.append(guessed_letter)
                success_letter.append(guessed_letter)
                semihashed_word = [letter if letter in success_letter else '-' for letter in word]
                print(semihashed_word)
                if '-' not in semihashed_word:
                    print(win)
                    break
        elif guessed_letter not in word:
            if guessed_letter in used_letter:
                print("this letter was already used")
            else:
                print(f"wrong guess, amount of lives left:{lives - 1}")
                lives -= 1
                used_letter.append(guessed_letter)
        else:
            print("something is wrong. Exiting \n")


word = select_word()
game_logic(word)
