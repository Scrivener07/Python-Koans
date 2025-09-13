"""
Provides unit testing for koan 1.
"""
import unittest
from unittest.mock import patch
import io
#--------------------------------------------------
from koans.testing import KoanTester
from . import solution
#--------------------------------------------------

class Testing(unittest.TestCase):

    # Data Types and Variables
    #--------------------------------------------------

    def test_challenge_01(self):
        self.assertIsInstance(solution.challenge_01(), bool)
        self.assertTrue(solution.challenge_01())


    def test_challenge_02(self):
        self.assertIsInstance(solution.challenge_02(), int)
        self.assertEqual(solution.challenge_02(), 42)


    def test_challenge_03(self):
        self.assertIsInstance(solution.challenge_03(), float)
        self.assertEqual(solution.challenge_03(), 3.14)


    def test_challenge_04(self):
        self.assertIsInstance(solution.challenge_04(), str)
        self.assertEqual(solution.challenge_04(), "Hello, World!")


    # Arithmetic Operations
    #--------------------------------------------------

    def test_challenge_05(self):
        self.assertEqual(solution.challenge_05(2, 3), 5)


    def test_challenge_06(self):
        self.assertEqual(solution.challenge_06(5, 2), 3)


    def test_challenge_07(self):
        self.assertEqual(solution.challenge_07(4, 3), 12)


    def test_challenge_08(self):
        self.assertEqual(solution.challenge_08(10, 2), 5.0)


    def test_challenge_09(self):
        self.assertEqual(solution.challenge_09(10, 3), 1)


    def test_challenge_10(self):
        self.assertEqual(solution.challenge_10(2, 3), 8)


    # String Operations
    #--------------------------------------------------

    def test_challenge_11(self):
        self.assertEqual(solution.challenge_11("Hello", "World"), "HelloWorld")


    def test_challenge_12(self):
        self.assertEqual(solution.challenge_12("AI!", 5), "AI!AI!AI!AI!AI!")


    # Type Conversion
    #--------------------------------------------------

    def test_challenge_13(self):
        self.assertEqual(solution.challenge_13("42"), 42)


    def test_challenge_14(self):
        self.assertEqual(solution.challenge_14("3.14"), 3.14)


    def test_challenge_15(self):
        self.assertEqual(solution.challenge_15(100), "100")


    def test_challenge_16(self):
        self.assertEqual(solution.challenge_16(0.85), "0.85")


    # Standard Input/Output
    #--------------------------------------------------

    def test_challenge_17(self):
        with patch('sys.stdout', new=io.StringIO()) as stdout:
            solution.challenge_17()
            data = stdout.getvalue().strip()
            self.assertEqual(data, "Hello, World!")



# Entry Point
#--------------------------------------------------
if __name__ == "__main__":
    KoanTester.execute()
