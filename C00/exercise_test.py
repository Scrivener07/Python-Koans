import unittest
#--------------------------------------------------
from . import solution as exercise
#--------------------------------------------------

class TestC00(unittest.TestCase):

    def test_hello_world(self):
        self.assertEqual(exercise.hello_string(), "Hello, World!")

    def test_add_two_numbers(self):
        self.assertEqual(exercise.add_two_numbers(2, 3), 5)
        self.assertEqual(exercise.add_two_numbers(-1, 1), 0)

    def test_subtract_two_numbers(self):
        self.assertEqual(exercise.subtract_two_numbers(2, 3), -1)
        self.assertEqual(exercise.subtract_two_numbers(-1, 5), -6)


if __name__ == "__main__":
    unittest.main()
