import unittest
import sys
import os
sys.path.append(os.getcwd() + "/part_1/src/") # noqa
from codemaker import Codemaker


class Tests(unittest.TestCase):

    # fail: code is nothing, pass: otherwise
    def test_there_is_code(self):
        self.coder = Codemaker()
        self.assertIsNotNone(self.coder._make_code())


if __name__ == '__main__':
    unittest.main()
