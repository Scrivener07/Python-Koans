"""
Provides unit testing for koan 2.
"""
import unittest
#--------------------------------------------------
from koans.testing import KoanTester
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
        self.assertEqual(solution.challenge_05(5), ["1", "2", "Fizz", "4", "Buzz"])
        self.assertEqual(solution.challenge_05(15)[14], "FizzBuzz")


    def test_challenge_06(self):
        self.assertEqual(solution.challenge_06(3), [3, 2, 1])
        self.assertEqual(solution.challenge_06(1), [1])


    def test_challenge_07(self):
        self.assertEqual(solution.challenge_07(95), "Excellent")
        self.assertEqual(solution.challenge_07(80), "Good")
        self.assertEqual(solution.challenge_07(65), "Pass")
        self.assertEqual(solution.challenge_07(50), "Fail")



# Entry Point
#--------------------------------------------------
if __name__ == "__main__":
    KoanTester.execute()
