"""
Provides unit testing for koan 0.

Use this import to target exercise testing.
    `from . import exercise`

Use this import to target solution testing.
    `from . import solution as exercise`
"""
import unittest
from unittest.mock import patch
import io
#--------------------------------------------------
from . import solution as exercise
#--------------------------------------------------

class Testing(unittest.TestCase):

    # Challenge 1
    def test_challenge_01(self):
        self.assertEqual(exercise.challenge_01(), "Hello, World!")


    # Challenge 2
    def test_challenge_02(self):
        self.assertEqual(exercise.challenge_02(), "Python!")


    # Challenge 3
    def test_challenge_03(self):
        with patch('sys.stdout', new=io.StringIO()) as stdout:
            exercise.challenge_03()
            data = stdout.getvalue().strip()
            self.assertEqual(data, "Hello, World!")


    # Challenge 4
    def test_challenge_04(self):
        with patch('sys.stdout', new=io.StringIO()) as stdout:
            exercise.challenge_04()
            data = stdout.getvalue().strip()
            self.assertEqual(data, "Python!")


    # Challenge 5
    def test_challenge_05(self):
        self.assertEqual(exercise.challenge_05(2, 3), 5)
        self.assertEqual(exercise.challenge_05(-1, 1), 0)


    # Challenge 6
    def test_challenge_06(self):
        self.assertEqual(exercise.challenge_06(2, 3), -1)
        self.assertEqual(exercise.challenge_06(-1, 5), -6)


if __name__ == "__main__":
    unittest.main()
