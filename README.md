# HANGMAN GAME

Hangman game is a python terminal game, that is currently being deployed into HEROKU terminal and fully playable.

The player needs to guess a word within a limit of 5 attempts. If the player cannot guess within this constraint, their character dies.

## How to play

Within an intro of the game, a word will be hidden but the player can see the amount of characters the word contains. 

The player can then guess a letter, not a number or special character, that might be in the word. Incorrect guess will result in loss of life, which is being graphically displayed to the player.

Shall the player be victorious, a trophy will be awarded.

## Features

* Random word generator. 
* Word is encrypted, so the player cannot see it straight away
* If player guess wrong letter, it shows list of previously guessed words
* If player guess correct letter, it will display those letters and keep rest encrypted
* Validation for duplicate entries, numbers and special characters
* Amount of lives is not changing if duplicate letter was guessed

## Testing

* Peers and friends used for testing functionality
* Tested for all possible scenarios with incorrect guesses
* Tested for all scenarios with successful guess
* Tested for all scenarios with special characters and letters
* Tested for empty input

### PEP8 valitated with no errors

## Bugs

    1. Special characters (*!"£$%^^& etc.) were possible
        - original solution of using list of banned characters was no longer feasible. isalpha() method was implemented to address this bug
    2. Throughout testing, multiple letters could be entered by the player
        - new condition created that checks for amount of letters
    3. On Heroku, initial encrypted word does not seem to be displaying spaces between characters, resulting in unclear word guess
        - fixed by adding spaces between letters
    4. Some lines are too long
        - fixed indentation and line breaks as per PEP8

## No other known bugs

# Deployment
    This project was deployed onto Heroku

## Steps
    - Create Heroku App
    - Set the buildbacks to python and NodeJS
    - link Heroku app to the repository
    - Deploy manually

# Credits

    - https://www.youtube.com/watch?v=cJJTnI22IF8&t=2s&ab_channel=KylieYing - this was used to understand the logic behind hiding characters in the word
    - https://www.tutorialspoint.com/python/string_isalpha.htm - for isalpha() method and its uses
    - https://www.w3schools.com/python/ref_string_upper.asp - for upper() method to keep user input in uppercase
    - https://ascii.co.uk/art - ASCII art taken from here


-----
Happy coding!