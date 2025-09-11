"""
Welcome to the module 1 unit exercise.

Please provide a solution for each coding challenge.
"""


# Data Types and Variables
def get_boolean():
    """Return a `true` boolean value."""
    return True


def get_integer():
    """Return the integer value `42`."""
    return 42


def get_float():
    """Return the float value `3.14`."""
    return 3.14


def get_string():
    """Return the string value `Hello, World!`."""
    return "Hello, World!"


# Arithmetic Operations
def add(x, y):
    """Return the value of `x` and `y` summed."""
    return x + y

def subtract(x, y):
    """Return the value of `x` and `y` subtracted."""
    return x - y

def multiply(x, y):
    """Return the value of `x` and `y` multiplied."""
    return x * y

def divide(x, y):
    """Return the value of `x` divided by `y`."""
    return x / y

def modulo(x, y):
    """Return the value of `x` modulo `y`."""
    return x % y

def exponentiate(base, exp):
    """Return the value of `base` raised to the power of `exp`."""
    return base ** exp


# String Operations
def concatenate(text_1, text_2):
    """Return the concatenation of `text_1` and `text_2`."""
    return text_1 + text_2

def repeat_string(text, number):
    """Return the string `text` repeated `number` times."""
    return text * number


# Type Conversion
def str_to_int(text):
    """Return the given `str` value as a `int` type value."""
    return int(text)

def str_to_float(text):
    """Return the given `str` value as a `float` type value."""
    return float(text)

def int_to_str(value_int):
    """Return the given `int` value as a `str` type value."""
    return str(value_int)

def float_to_str(value_float):
    """Return the given `float` value as a `str` type value."""
    return str(value_float)


# Standard Input/Output
def console_print_hello():
    """Print the message 'Hello, World!' to console exactly as shown using the `print()` function."""
    print("Hello, World!")
