"""
Provides unit testing for koan 0.
"""
import unittest
from unittest.mock import patch
import io
#--------------------------------------------------
from koans.testing import KoanTester
from . import solution
#--------------------------------------------------

class Testing(unittest.TestCase):


    # Returning Values
    #--------------------------------------------------

    def test_challenge_01(self):
        self.assertEqual(solution.challenge_01(), "Hello, World!")


    def test_challenge_02(self):
        self.assertEqual(solution.challenge_02(), "Python!")


    # Printing Output
    #--------------------------------------------------

    def test_challenge_03(self):
        with patch('sys.stdout', new=io.StringIO()) as stdout:
            solution.challenge_03()
            data = stdout.getvalue().strip()
            self.assertEqual(data, "Hello, World!")


    def test_challenge_04(self):
        with patch('sys.stdout', new=io.StringIO()) as stdout:
            solution.challenge_04()
            data = stdout.getvalue().strip()
            self.assertEqual(data, "Python!")


    # Arithmetic Operations
    #--------------------------------------------------

    def test_challenge_05(self):
        self.assertEqual(solution.challenge_05(2, 3), 5)
        self.assertEqual(solution.challenge_05(-1, 1), 0)


    def test_challenge_06(self):
        self.assertEqual(solution.challenge_06(2, 3), -1)
        self.assertEqual(solution.challenge_06(-1, 5), -6)



# Entry Point
#--------------------------------------------------
if __name__ == "__main__":
    KoanTester.execute()
