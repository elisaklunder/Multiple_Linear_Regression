# OOP - 2023/24 - Assignment 2


## Your report
to do:
- write report for and p2


## Part 1

**Codemaker
Manages Mastermind's solution with private attributes _colors and _code (which should therefore not be modified by the user) and public attribute max_iterations, set by the user at the start of the game.

Methods:

_guess_errors(): raises errors on the user input. Private because the guess format is given at the beginning and should not be modified.

_make_code(self): generates a random combination of code. Private since the secret code should not be modified by the user.

get_code(): provides a way for the user to retrieve the secret code. Public because it allows users to access the value of the secret code safely.

_correct_guesses_right_pos() and _correct_guesses_wrong_pos(): compare a guess with the secret code and return the number of correct guesses in the right/wrong position. Private becasue internal details of the code evaluation process should be kept hidden from the user.

**Mastermind
Inherits from Codemaker and runs the actual game. Its attributes are inherited from Codemaker.
The additional methods are:

_formatting_guess(): ensures that the input given by the user is converted to uppercase. Private because internal details of the game's input processing shouldn't be public.

game(): public method that is called in the main and takes care of carrying out the game. It generates the secret code, prompts the user to input their guesses, receives user input guesses, and provides feedback to the user. After the max_iterations iterations are complete, the correct answer is revealed.
