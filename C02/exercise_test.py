"""
Provides unit testing for koan 2.

Use this import to target exercise testing.
    `from . import exercise`

Use this import to target solution testing.
    `from . import solution as exercise`
"""
import unittest
#--------------------------------------------------
from . import solution as exercise
#--------------------------------------------------

class Testing(unittest.TestCase):

    def test_challenge_01(self):
        self.assertEqual(exercise.challenge_01(2, 3), 5)
        self.assertEqual(exercise.challenge_01(-1, 1), 0)


    def test_challenge_02(self):
        self.assertTrue(exercise.challenge_02(5, 2))
        self.assertFalse(exercise.challenge_02(2, 5))
        self.assertFalse(exercise.challenge_02(3, 3))


    def test_challenge_03(self):
        self.assertTrue(exercise.challenge_03(True, True))
        self.assertFalse(exercise.challenge_03(True, False))
        self.assertFalse(exercise.challenge_03(False, True))
        self.assertFalse(exercise.challenge_03(False, False))


    def test_challenge_04(self):
        self.assertEqual(exercise.challenge_04(5), 6)
        self.assertEqual(exercise.challenge_04(-1), 0)


    def test_challenge_05(self):
        self.assertEqual(exercise.challenge_05(5), ["1", "2", "Fizz", "4", "Buzz"])
        self.assertEqual(exercise.challenge_05(15)[14], "FizzBuzz")


    def test_challenge_06(self):
        self.assertEqual(exercise.challenge_06(3), [3, 2, 1])
        self.assertEqual(exercise.challenge_06(1), [1])


    def test_challenge_07(self):
        self.assertEqual(exercise.challenge_07(95), "Excellent")
        self.assertEqual(exercise.challenge_07(80), "Good")
        self.assertEqual(exercise.challenge_07(65), "Pass")
        self.assertEqual(exercise.challenge_07(50), "Fail")


if __name__ == "__main__":
    unittest.main()
