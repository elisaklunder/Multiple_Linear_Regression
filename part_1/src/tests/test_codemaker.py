import os
import sys
import unittest

sys.path.append(os.getcwd() + "/part_1/src/")
from codemaker import Codemaker


class Tests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.coder = Codemaker()

    def test_there_is_code(self):
        """
        fail: code is nothing (None), pass: otherwise
        """
        self.assertIsNotNone(self.coder._make_code())

    def test_code_is_strings(self):
        """
        fail: code is not a set of strings, pass: otherwise
        """
        code = self.coder._make_code()
        self.assertTrue(all(isinstance(element, str) for element in code))

    def test_code_has_4_elements(self):
        """
        fail: code doesn't have len = 4, pass: otherwise
        """
        code = self.coder._make_code()
        self.assertTrue(len(code) == 4)

    def test_correct_guesses_right_pos_is_number(self):
        """
        fail: the _correct_guesses_right_pos_ doesn't return a number
        pass: otherwise
        """
        guess = ["B", "B", "Y", "R"]
        self.assertIsInstance(
            self.coder._correct_guesses_right_pos(guess), int
        )

    def test_guess_has_correct_colors(self):
        """
        fail: the guess passed to the _correct_guesses_right_pos_ function
        doesn't have valid colors
        pass: otherwise
        """
        guess = ["B", "Y", "B", "J"]
        self.assertRaises(
            TypeError, self.coder._correct_guesses_right_pos, guess
        )

    def test_guess_has_incorrect_length(self):
        """
        fail: the guess passed to the _correct_guesses_right_pos_ function is
        the right length since the error is not raised
        pass: if length is incorrect the error is raised
        """
        guess = ["B", "Y", "B"]
        self.assertRaises(
            ValueError, self.coder._correct_guesses_right_pos, guess
        )

    def test_correct_number_returened_right_pos(self):
        """
        fail: if the funciton _correct_guesses_right_pos(guess) returns the
        wrong number of correct guesses
        pass: otherwise
        """
        self.coder._code = ["B", "Y", "B", "R"]
        guess = ["B", "B", "R", "G"]
        self.assertEqual(self.coder._correct_guesses_right_pos(guess), 1)

    def test_correct_number_returened_wrong_pos(self):
        """
        fail: if the function _correct_guesses_wrong_pos(guess) returns the
        incorrect number
        pass: otherwise
        """
        self.coder._code = ["B", "Y", "B", "G"]
        guess = ["B", "W", "B", "Y"]
        self.assertEqual(self.coder._correct_guesses_wrong_pos(guess), 1)

    def test_max_iterations(self):
        """
        fail: if the maximum number of terations is not an int
        pass: if the value is an int or if it is not specified by the user
        """
        self.coder.max_iterations = 3
        self.assertIsInstance(self.coder.max_iterations, int)

    def test_exception_right_col_wrong_pos(self):
        """
        EXCEPTION!
        fail: if the number of returned colors is wrong (in this case the last
        B, shouldn't be considered as a right guess in the wrong position,
        since the B is already matched)
        pass: otherwise
        """
        self.coder._code = ["B", "W", "B", "G"]
        guess = ["B", "W", "B", "B"]
        self.assertEqual(self.coder._correct_guesses_wrong_pos(guess), 0)

    def test_max_iterations1(self):
        """
        pass: if when the maximum number of terations is not an int the
        program doesn't raise an error
        fail: when the error is not raised
        """
        max_iterations = "a"
        self.assertRaises(TypeError, self.coder.__init__, max_iterations)

    def test_max_iterations2(self):
        """
        fail: if the maximum number of iteration is not a number smaller
        than 0, since the error is not raised
        pass: if the error is raised
        """
        max_iterations = -3
        self.assertRaises(TypeError, self.coder.__init__, max_iterations)


if __name__ == "__main__":
    unittest.main()
