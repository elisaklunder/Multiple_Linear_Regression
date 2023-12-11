import unittest
import sys
import os
sys.path.append(os.getcwd() + "/part_1/src/")
from codemaker import Codemaker


class Tests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.coder = Codemaker()

    # fail: code is nothing, pass: otherwise
    def test_there_is_code(self):
        self.assertIsNotNone(self.coder._make_code())

    # fail: code is not a set of strings, pass: otherwise
    def test_code_is_strings(self):
        code = self.coder._make_code()
        self.assertTrue(all(isinstance(element, str) for element in code))

    # fail: code doesn't have len = 4, pass: otherwise
    def test_code_has_4_elements(self):
        code = self.coder._make_code()
        self.assertTrue(len(code) == 4)

    # fail: the _correct_guesses_right_pos_ doesn't return a number, pass:
    # otherwise
    def test_correct_guesses_right_pos_is_number(self):
        guess = ["B", "B", "Y", "R"]
        self.assertIsInstance(self.coder._correct_guesses_right_pos(guess),
                              int)

    # fail: the guess passed to the _correct_guesses_right_pos_ function
    # doesn't have valid colors, pass: otherwise
    def test_guess_has_correct_colors(self):
        guess = ["B", "Y", "B", "J"]
        self.assertRaises(TypeError,
                          self.coder._correct_guesses_right_pos, guess)

    # fail: the guess passed to the _correct_guesses_right_pos_ function
    # is the right length since the error is not raised,
    # pass: if length is incorrect the error is raised
    def test_guess_has_incorrect_length(self):
        guess = ["B", "Y", "B"]
        self.assertRaises(ValueError,
                          self.coder._correct_guesses_right_pos, guess)

    # fail: if the funciton _correct_guesses_right_pos(guess) returns the
    # wrong number of correct guesses
    # pass: otherwise
    def test_correct_number_returened_right_pos(self):
        self.coder._code = ["B", "Y", "B", "R"]
        guess = ["B", "B", "R", "G"]
        self.assertEqual(self.coder._correct_guesses_right_pos(guess), 1)

    # fails: if the function _correct_guesses_wrong_pos(guess) returns the
    # incorrect number
    # pass: otherwise
    def test_correct_number_returened_wrong_pos(self):
        self.coder._code = ["B", "Y", "B", "R"]
        guess = ["B", "B", "K", "R"]
        self.assertEqual(self.coder._correct_guesses_wrong_pos(guess), 1)

    def test_max_iterations(self):
        self.coder.max_iterations = "one"
        self.assertIsInstance(self.coder.max_iterations, int)


if __name__ == '__main__':
    unittest.main()
