import unittest
import sys
import os
sys.path.append(os.getcwd() + "/part_1/src/")
from codemaker import Codemaker


class Tests(unittest.TestCase):

    def test_there_is_code(self):
        coder = Codemaker()
        self.assertIsNotNone(coder.make_code())

        pass
    pass


if __name__ == '__main__':
    unittest.main()
