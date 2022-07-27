import random

print(f'Welcome to Hangman game')

words = ("apple", "banana", "cherry")
banned_characters = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")

wrong_letter = []
correct_letter = []


def select_word():
    """
    Randomly selected word from list of words
    """
    selected_word = random.choice(words)
    return selected_word


def guess_letter():
    """
    User selects a letter
    """
    while True:
        chosen_letter = input(f"Choose a letter: \n")    
        if validate_letter(chosen_letter):
            print("Data is valid!")
            break

    return chosen_letter


def validate_letter(letter):
    """
    A validation function, that checks that user input is correct
    list of banned characters is being used to prevent user to 
    waste their attempts by using characters that are never going
    to be used.
    """
    try:
        
        if len(letter) != 1:
            raise ValueError(
                f"You can guess only single letter, you provided {len(letter)}"
            )
        for character in banned_characters:
            if letter == character:
                raise ValueError(
                    f"You can guess only letters, you provided number: {letter}"
                )
    except ValueError as error:
        print(f"Invalid data: {error}, please try again.\n")
        return False

    return True


def game_logic(word, chosen_letter):
    print(f"{word} from correct letter fun")
    print(f"{chosen_letter} from correct letter fun")
    word_list = list(word)
    while wrong_letter < 5 and correct_letter < 5:
        if chosen_letter in word_list:
            print("yay")
            correct_letter.append(chosen_letter)
        else:
            print("nay")
            wrong_letter.append(chosen_letter)


word = select_word()
chosen_letter = (guess_letter())
game_logic(word, chosen_letter)

used_letters = wrong_letter + correct_letter
print(f"{correct_letter} - correct letters")
print(f"{wrong_letter} -wrong letters")
print(f"{used_letters} - all letters")

