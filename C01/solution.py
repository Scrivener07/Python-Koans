"""
Welcome to koan exercise 1.

Please provide a solution for each coding challenge.
"""
from koans import koan


# Challenge 1
#--------------------------------------------------
@koan
def challenge_01():
    """
    Return a `true` boolean value.
    """
    return True


# Challenge 2
#--------------------------------------------------
@koan
def challenge_02():
    """
    Return the integer value `42`.
    """
    return 42


# Challenge 3
#--------------------------------------------------
@koan
def challenge_03():
    """
    Return the float value `3.14`.
    """
    return 3.14


# Challenge 4
#--------------------------------------------------
@koan
def challenge_04():
    """
    Return the string value `Hello, World!`.
    """
    return "Hello, World!"


# Challenge 5
#--------------------------------------------------
@koan
def challenge_05(x, y):
    """
    Return the value of `x` and `y` summed.
    """
    return x + y


# Challenge 6
#--------------------------------------------------
@koan
def challenge_06(x, y):
    """
    Return the value of `x` and `y` subtracted.
    """
    return x - y


# Challenge 7
#--------------------------------------------------
@koan
def challenge_07(x, y):
    """
    Return the value of `x` and `y` multiplied.
    """
    return x * y


# Challenge 8
#--------------------------------------------------
@koan
def challenge_08(x, y):
    """
    Return the value of `x` divided by `y`.
    """
    return x / y


# Challenge 9
#--------------------------------------------------
@koan
def challenge_09(x, y):
    """
    Return the value of `x` modulo `y`.
    """
    return x % y


# Challenge 10
#--------------------------------------------------
@koan
def challenge_10(base, exp):
    """
    Return the value of `base` raised to the power of `exp`.
    """
    return base ** exp


# Challenge 11
#--------------------------------------------------
@koan
def challenge_11(text_1, text_2):
    """
    Return the concatenation of `text_1` and `text_2`.
    """
    return text_1 + text_2


# Challenge 12
#--------------------------------------------------
@koan
def challenge_12(text, number):
    """
    Return the string `text` repeated `number` times.
    """
    return text * number


# Challenge 13
#--------------------------------------------------
@koan
def challenge_13(text):
    """
    Return the given `str` value as a `int` type value.
    """
    return int(text)


# Challenge 14
#--------------------------------------------------
@koan
def challenge_14(text):
    """
    Return the given `str` value as a `float` type value.
    """
    return float(text)


# Challenge 15
#--------------------------------------------------
@koan
def challenge_15(value_int):
    """
    Return the given `int` value as a `str` type value.
    """
    return str(value_int)


# Challenge 16
#--------------------------------------------------
@koan
def challenge_16(value_float):
    """
    Return the given `float` value as a `str` type value.
    """
    return str(value_float)


# Challenge 17
#--------------------------------------------------
@koan
def challenge_17():
    """Print the message `Hello, World!` to console exactly as shown using the `print()` function."""
    print("Hello, World!")


# Challenge 18
#--------------------------------------------------
@koan
def challenge_18(numbers):
    """
    Challenge: Sum of List

    Instructions:
        Return the sum of all numbers in the provided list.

    Sample Data:
        Input: [1, 2, 3]
        Output: 6

    Result Format:
        Return the result as an integer.

    Concepts:
        List iteration, sum function

    Returns:
        int: The sum of the numbers
    """
    return sum(numbers)


# Challenge 19
#--------------------------------------------------
@koan
def challenge_19(text):
    """
    Challenge: String Length

    Instructions:
        Return the length of the provided string.

    Sample Data:
        Input: "Python"
        Output: 6

    Result Format:
        Return the result as an integer.

    Concepts:
        String, len() function

    Returns:
        int: The length of the string
    """
    return len(text)


# Challenge 20
#--------------------------------------------------
@koan
def challenge_20(number):
    """
    Challenge: Even or Odd

    Instructions:
        Return "Even" if the number is even, "Odd" otherwise.

    Sample Data:
        Input: 4
        Output: "Even"
        Input: 7
        Output: "Odd"

    Result Format:
        Return the result as a string.

    Concepts:
        Modulo operator, conditional statements

    Returns:
        str: "Even" or "Odd"
    """
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"



# Challenge 21
#--------------------------------------------------
@koan
def challenge_21():
    """
    Challenge: Print a Friendly Message

    Instructions:
        Print "Welcome to Python Koans!" to the console.

    Sample Data:
        Output: Welcome to Python Koans!

    Result Format:
        Print the result using the print() function.

    Concepts:
        Standard output, print function

    Returns:
        None
    """
    print("Welcome to Python Koans!")


# Challenge 22
#--------------------------------------------------
@koan
def challenge_22(a, b):
    """
    Challenge: Maximum Value

    Instructions:
        Return the greater of two numbers.

    Sample Data:
        Input: 3, 5
        Output: 5

    Result Format:
        Return the result as an integer.

    Concepts:
        Conditional statements, comparison operators

    Returns:
        int: The greater value
    """
    return max(a, b)
