import unittest
import sys
import os
sys.path.append(os.getcwd() + "/part_1/src/") # noqa
from codemaker import Codemaker


class Tests(unittest.TestCase):

    # fail: code is nothing, pass: otherwise
    def test_there_is_code(self):
        coder = Codemaker()
        self.assertIsNotNone(coder._make_code())

    # fail: code is not a set of strings, pass: otherwise
    def test_code_is_strings(self):
        coder = Codemaker()
        code = coder._make_code()
        self.assertTrue(all(isinstance(element, str) for element in code))


if __name__ == '__main__':
    unittest.main()
