import unittest
#--------------------------------------------------
from . import solution as exercise
#--------------------------------------------------

class TestM02(unittest.TestCase):

    def test_add_numbers(self):
        self.assertEqual(exercise.add_numbers(2, 3), 5)
        self.assertEqual(exercise.add_numbers(-1, 1), 0)


    def test_is_greater(self):
        self.assertTrue(exercise.is_greater(5, 2))
        self.assertFalse(exercise.is_greater(2, 5))
        self.assertFalse(exercise.is_greater(3, 3))


    def test_both_true(self):
        self.assertTrue(exercise.both_true(True, True))
        self.assertFalse(exercise.both_true(True, False))
        self.assertFalse(exercise.both_true(False, True))
        self.assertFalse(exercise.both_true(False, False))


    def test_assign_and_increment(self):
        self.assertEqual(exercise.assign_and_increment(5), 6)
        self.assertEqual(exercise.assign_and_increment(-1), 0)


    def test_fizzbuzz(self):
        self.assertEqual(
            exercise.fizzbuzz(5),
            ["1", "2", "Fizz", "4", "Buzz"]
        )
        self.assertEqual(
            exercise.fizzbuzz(15)[14],
            "FizzBuzz"
        )


    def test_count_down(self):
        self.assertEqual(exercise.count_down(3), [3, 2, 1])
        self.assertEqual(exercise.count_down(1), [1])


    def test_grade_message(self):
        self.assertEqual(exercise.grade_message(95), "Excellent")
        self.assertEqual(exercise.grade_message(80), "Good")
        self.assertEqual(exercise.grade_message(65), "Pass")
        self.assertEqual(exercise.grade_message(50), "Fail")


# Allows test to be run from command line in additional to VS Code Test Explorer.
if __name__ == "__main__":
    unittest.main()
