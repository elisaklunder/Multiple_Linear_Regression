import random


class Codemaker:
    def __init__(self) -> None:
        self._code = []
        self._colors = ["W", "K", "Y", "G", "R", "B"]

    def _guessErrors(self, guess):
        if len(guess) != 4:
            raise ValueError("The guess must be a list of four elements.")

        if not all(element in self._colors for element in guess):
            raise TypeError('Invalid guess elements. The only valid guess \
                            elements are "W", "K", "Y", "G", "R", "B"')
        pass

    def _make_code(self):
        self._code = random.choices(self._colors, k=4)
        return self._code

    def _correct_guesses_right_pos(self, guess):
        self._guessErrors(guess)
        number = 0
        for colors in range(len(guess)):
            if guess[colors] == self._code[colors]:
                number += 1
        return number

    def _correct_guesses_wrong_pos(self, guess):
        self._guessErrors(guess)
        number = 0
        i = 0
        for colors in guess:
            if colors in self._code and guess[i] != self._code[i]:
                number += 1
            i += 1
        return number

    # max number of attempt
    # lower to higher case
