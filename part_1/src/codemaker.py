import random


class Codemaker:
    def __init__(self, max_iterations: int = 1) -> None:
        self._code = []
        self._colors = ["W", "K", "Y", "G", "R", "B"]
        if not isinstance(max_iterations, int):
            raise TypeError("max iterations should be an int value")
        self.max_iterations = max_iterations

    def _guess_errors(self, guess: list[str]) -> None:
        """
        Args:
            guess: list containg string with the guesses

        Raises:
            ValueError when the number of elements is not four
            TypeError when the guess is not in a valid format
        """
        if len(guess) != 4:
            raise ValueError("The guess must be a list of four elements.")

        if not all(element in self._colors for element in guess):
            raise TypeError('Invalid guess elements. The only valid guess \
                            elements are "W", "K", "Y", "G", "R", "B"')
        pass

    def _make_code(self) -> list[str]:
        """
        Returns:
            list with strings containing 4 random choises of possible colors
        """
        self._code = random.choices(self._colors, k=4)
        return self._code

    def get_code(self) -> list[str]:
        return self._code

    def _correct_guesses_right_pos(self, guess: list[str]) -> int:
        """
        Args:
            guess: list containg 4 string with the guesses
        Returs:
            number: an int displaying the number of correct guesses
            in the right position
        Raises:
            errors as described in the private method _guess_errors
        """
        self._guess_errors(guess)
        number = 0
        for colors in range(len(guess)):
            if guess[colors] == self._code[colors]:
                number += 1
        return number

    def _correct_guesses_wrong_pos(self, guess: list[str]) -> int:
        """
        Args:
            guess: list containg 4 string with the guesses
        Returs:
            number: an int displaying the number of correct guesses but
            in the wrong position
        Raises:
            errors as described in the private method _guess_errors
        """
        self._guess_errors(guess)
        number = 0
        for colors in guess:
            if colors in self._code and guess.index(colors) != self._code.index(colors):
                number += 1
        return number
