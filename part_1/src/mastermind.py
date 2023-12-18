from codemaker import Codemaker


class Mastermind(Codemaker):
    def formatting_guess(self, guess: str) -> str:
        """
        formats the initial guess

        Args:
            guess (str): list containg string with the guesses

        Returns:
            str: a string in higher case to make sure that the
            colors typed in the input can be matched
        """
        return guess.upper()

    def game(self) -> None:
        """
        method that takes care of carrying out the game, taking the user input
        """
        self._make_code()

        for i in range(self.max_iterations):
            guess_input = input(
                "type the initial of the colors\
 of the guesses separated by a space: "
            )
            guess = self.formatting_guess(guess_input)
            guess = guess.split()

            wrong_position = self._correct_guesses_wrong_pos(guess)
            right_position = self._correct_guesses_right_pos(guess)

            print(
                f"the number of guesses in the right position\
 with the right color is: {right_position}"
            )
            print(
                f"the number of guesses in the wrong position\
 with the right color is: {wrong_position}"
            )

        print(f"the correct answer is {self.get_code()}")
        pass
