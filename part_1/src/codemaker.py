import random


class Codemaker:
    def __init__(self) -> None:
        self.code = []
        self.guess = []
        self._colors = ["W", "K", "Y", "G", "R", "B"]

    def make_code(self):
        self.code = random.choices(self._colors, k=10)
        
