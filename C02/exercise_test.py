"""
Provides unit testing for koan 2.
"""
import unittest
#--------------------------------------------------
from koans.testing import KoanLauncher
from . import solution
#--------------------------------------------------

class Testing(unittest.TestCase):

    def test_challenge_01(self):
        self.assertEqual(solution.challenge_01(2, 3), 5)
        self.assertEqual(solution.challenge_01(-1, 1), 0)


    def test_challenge_02(self):
        self.assertTrue(solution.challenge_02(5, 2))
        self.assertFalse(solution.challenge_02(2, 5))
        self.assertFalse(solution.challenge_02(3, 3))


    def test_challenge_03(self):
        self.assertTrue(solution.challenge_03(True, True))
        self.assertFalse(solution.challenge_03(True, False))
        self.assertFalse(solution.challenge_03(False, True))
        self.assertFalse(solution.challenge_03(False, False))


    def test_challenge_04(self):
        self.assertEqual(solution.challenge_04(5), 6)
        self.assertEqual(solution.challenge_04(-1), 0)


    def test_challenge_05(self):
        data:list[str] = [
            "1",
            "2",
            "Fizz",
            "4",
            "Buzz",
            "Fizz",
            "7",
            "8",
            "Fizz",
            "Buzz",
            "11",
            "Fizz",
            "13",
            "14",
            "FizzBuzz"
        ]
        self.assertEqual(solution.challenge_05(5), data[0:5])
        self.assertEqual(solution.challenge_05(10), data[0:10])
        self.assertEqual(solution.challenge_05(15), data)


    def test_challenge_06(self):
        self.assertEqual(solution.challenge_06(3), [3, 2, 1])
        self.assertEqual(solution.challenge_06(1), [1])


    def test_challenge_07(self):
        self.assertEqual(solution.challenge_07(95), "Excellent")
        self.assertEqual(solution.challenge_07(80), "Good")
        self.assertEqual(solution.challenge_07(65), "Pass")
        self.assertEqual(solution.challenge_07(50), "Fail")


    def test_challenge_08(self):
        negative:list[int] = [0, 1, 2, 3, 4, 5]
        self.assertEqual(solution.challenge_08(negative), 6)
        positive:list[int] = [0, -1, -2, -3, -4, -5]
        self.assertEqual(solution.challenge_08(positive), -6)


    def test_challenge_09(self):
        positive:list[int] = [0, 1, 2, 3, 4, 5]
        self.assertEqual(solution.challenge_09(positive), 9)
        negative:list[int] = [0, -1, -2, -3, -4, -5]
        self.assertEqual(solution.challenge_09(negative), -9)



# Entry Point
#--------------------------------------------------
if __name__ == "__main__":
    KoanLauncher.execute()
