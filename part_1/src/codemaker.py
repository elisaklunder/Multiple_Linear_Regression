import random


class Codemaker:
    def __init__(self) -> None:
        self._code = []
        self.guess = []
        self._colors = ["W", "K", "Y", "G", "R", "B"]

    def _make_code(self):
        self._code = random.choices(self._colors, k=4)
        return self._code
