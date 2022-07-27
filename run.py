import random

print(f'Welcome to Hangman game')

words = ("apple", "banana", "cherry")
banned_characters = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")


def select_word():
    """
    Randomly selected word from list of words
    """
    selected_word = random.choice(words)
    return selected_word


def game_logic(word):
    word_list = list(word)
    wrong_letter = set()
    correct_letter = set()
    
    hashed_word = ['-' for letter in word_list]
    print("Guess the word", "".join(hashed_word))

    while len(word_list) > 0 and len(wrong_letter) < 5:
        chosen_letter = input("enter a letter \n")
        semihashed_word = [letter if letter in correct_letter else '-' for letter in word_list]
        print(''.join(semihashed_word))
        if chosen_letter in banned_characters:
            print("you can use only letters, numbers are not used")
        elif chosen_letter in wrong_letter.union(correct_letter):
            print("this letter was already guessed")
        elif len(chosen_letter) > 1:
            print(f"You can guess only single letter, you guessed {len(chosen_letter)}")
        elif len(chosen_letter) == 1:
            if chosen_letter in word:
                print("yay")
                correct_letter.add(chosen_letter)
                print('correct letters so far:', '-'.join(correct_letter))
                
            else:
                print("nay")
                wrong_letter.add(chosen_letter)
                guessed_letter = wrong_letter.union(correct_letter)
                print(f"So far you have tried these letters: {guessed_letter}")            
        
    # if len(wrong_letter) == 5:
    #     print("you lost")
    # elif len(word_list) == 0:
    #     print("you won!")
        

word = select_word()
game_logic(word)
