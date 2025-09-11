"""
Provides unit testing for module 1.

Use this import to target exercise testing.
    `import exercise`

Use this import to target solution testing.
    `import solution as exercise`
"""
import unittest
import io
from unittest.mock import patch
#--------------------------------------------------
from . import solution as exercise
#--------------------------------------------------

class TestM01(unittest.TestCase):

    # Data Types and Variables
    def test_get_integer(self):
        self.assertIsInstance(exercise.get_integer(), int)
        self.assertEqual(exercise.get_integer(), 42)

    def test_get_float(self):
        self.assertIsInstance(exercise.get_float(), float)
        self.assertEqual(exercise.get_float(), 3.14)

    def test_get_string(self):
        self.assertIsInstance(exercise.get_string(), str)
        self.assertEqual(exercise.get_string(), "Hello, World!")

    def test_get_boolean(self):
        self.assertIsInstance(exercise.get_boolean(), bool)
        self.assertTrue(exercise.get_boolean())


    # Arithmetic Operations
    def test_add(self):
        self.assertEqual(exercise.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(exercise.subtract(5, 2), 3)

    def test_multiply(self):
        self.assertEqual(exercise.multiply(4, 3), 12)

    def test_divide(self):
        self.assertEqual(exercise.divide(10, 2), 5.0)

    def test_modulo(self):
        self.assertEqual(exercise.modulo(10, 3), 1)

    def test_exponentiate(self):
        self.assertEqual(exercise.exponentiate(2, 3), 8)

    # String Operations
    def test_concatenate(self):
        self.assertEqual(exercise.concatenate("Hello", "World"), "HelloWorld")

    def test_repeat_string(self):
        self.assertEqual(exercise.repeat_string("AI!", 5), "AI!AI!AI!AI!AI!")

    # Type Conversion
    def test_str_to_int(self):
        self.assertEqual(exercise.str_to_int("42"), 42)

    def test_str_to_float(self):
        self.assertEqual(exercise.str_to_float("3.14"), 3.14)

    def test_int_to_str(self):
        self.assertEqual(exercise.int_to_str(100), "100")

    def test_float_to_str(self):
        self.assertEqual(exercise.float_to_str(0.85), "0.85")

    # Standard Input/Output
    def test_console_print_hello(self):
        # Mock the system standard output object for 'fake' called `stdout`.
        with patch('sys.stdout', new=io.StringIO()) as stdout:
            exercise.console_print_hello()
            data = stdout.getvalue().strip()
            self.assertEqual(data, "Hello, World!")


# Allows test to be run from command line in addition to the VS Code Test Explorer.
if __name__ == "__main__":
    unittest.main()
