import random


class Codemaker:
    def __init__(self) -> None:
        self._code = []
        self._colors = ["W", "K", "Y", "G", "R", "B"]

    def _make_code(self):
        self._code = random.choices(self._colors, k=4)
        return self._code

    # assume for now that guess is a valid guess
    def _correct_guesses_right_pos(self, guess):
        number = 2
        return number

    def _correct_guesses_wrong_pos(self, guess):
        pass
