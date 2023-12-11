import unittest
import sys
import os
sys.path.append(os.getcwd() + "/part_1/src/")
import codemaker


class Tests(unittest.TestCase):

    def test_there_is_code(self):
        self.assertIsNotNone(codemaker.make_code())

        pass
    pass
