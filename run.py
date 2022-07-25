import random

print(f'Welcome to Hangman game')

words = ("apple", "banana", "cherry")
banned_characters = ("1", "2")


def select_word():
    """
    Randomly selected word from list of words
    """
    selected_word = random.choice(words)
    print(selected_word)


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

    try:
        
        if len(letter) != 1:
            raise ValueError(
                f"You can guess only single letter, you provided {len(letter)}"
            )
        if letter == [thing for thing in banned_characters]:
            raise ValueError(
                f"You can guess only letters, you provided number: {letter}"
            )
    except ValueError as error:
        print(f"Invalid data: {error}, please try again.\n")
        return False

    return True

select_word()
chosen_letter = (guess_letter())

