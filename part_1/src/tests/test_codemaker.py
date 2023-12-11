import unittest
import sys
import os
sys.path.append(os.getcwd() + "/part_1/src/") # noqa
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

    def test_correct_guesses_right_pos_is_number(self):
        guess = ["B", "B", "Y", "R"]
        self.assertIsInstance(self.coder._correct_guesses_right_pos(guess),
                              int)

    def test_guess_has_correct_colors(self):
        guess = ["B", "J"]
        self.assertRaises(TypeError,
                          self.coder._correct_guesses_right_pos(guess))


if __name__ == '__main__':
    unittest.main()
