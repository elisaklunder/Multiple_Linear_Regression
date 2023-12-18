import random


class Codemaker:
    def __init__(self, max_iterations: int = 1) -> None:
        self._code = []
        self._colors = ["W", "K", "Y", "G", "R", "B"]
        if not isinstance(max_iterations, int):
            raise TypeError("max iterations should be an int value")

        if max_iterations < 1:
            raise TypeError(
                "The number of iterations has to be an integer \
greater than 0"
            )
        self.max_iterations = max_iterations

    def _guess_errors(self, guess: list[str]) -> None:
        """
        private method raising errors when the format of the input is incorrect

        Args:
            guess (list[str]): list containg string with the guesses

        Raises:
            ValueError: when the number of elements is not four
            TypeError: when the guess is not in a valid format
        """
        if len(guess) != 4:
            raise ValueError("The guess must be a list of four elements.")

        if not all(element in self._colors for element in guess):
            raise TypeError(
                'Invalid guess elements. The only valid guess \
elements are "W", "K", "Y", "G", "R", "B" divided by a space'
            )
        pass

    def _make_code(self) -> list[str]:
        """
        private method generating the code to brake

        Returns:
            list[str]: list with strings containing 4 random choises of
            possible colors
        """
        self._code = random.choices(self._colors, k=4)
        return self._code

    def get_code(self) -> list[str]:
        """
        method to get the code

        Returns:
            list[str]: returns the code
        """
        return self._code

    def _correct_guesses_right_pos(self, guess: list[str]) -> int:
        """
        private method that compares the guess with the code to be broken, and
        returns the number of correct guesses in the right position

        Args:
            guess (list[str]): list containg 4 string with the guesses

        Returns:
            int: number of correct guesses in the right position
        """
        self._guess_errors(guess)
        number = 0
        for colors in range(len(guess)):
            if guess[colors] == self._code[colors]:
                number += 1
        return number

    def _correct_guesses_wrong_pos(self, guess: list[str]) -> int:
        """
        private method that compares the guess with the code to be broken, and
        returns the number of correct guesses in the wrong position

        Args:
            guess (list[str]): list containg 4 string with the guesses

        Returns:
            int: displaying the number of correct guesses but in the wrong
            position
        """
        self._guess_errors(guess)
        number = 0
        for colors in guess:
            if colors in self._code and guess.index(
                colors
            ) != self._code.index(colors):
                number += 1
        return number
