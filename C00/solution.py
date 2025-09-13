"""
Welcome to the getting started primer for koan challenges.

Each challenge is a labeled group of Python code lines.
Your job: Fill in the blank below each label with your answer.

You do not need to understand how these labels work yet.
Just focus on writing the correct code for each challenge.
"""
from koans import koan

# Challenge 1
#--------------------------------------------------
# Most challenges will have you `return` a value.
# The word `return` is a special keyword in Python written as `return <value>`.
# The string "Hello, World!" here is the <value> for which you must return.
#
# You can think of the `return` keyword as how you submit your answer.
#
# In this first challenge, you are asked to return the string "Hello, World!".
# There is nothing to calculate, so we can just submit the literal string.
def challenge_01():
    """
    Return the string 'Hello, World!'.

    Returns:
        `str`: The string 'Hello, World!'.

    Hint:
        Use the `return` keyword followed by a string literal.
    """
    return "Hello, World!"


# Challenge 2: Now its your turn!
#--------------------------------------------------
@koan
def challenge_02():
    """
    Return the string 'Python!'.

    Hint:
        Look at the previous challenge.
    """
    return "Python!"



# Challenge 3
#--------------------------------------------------
# Sometimes a challenge won't require you to return a value at all.
#
# In this challenge you only need to `print()` the solution.
def challenge_03():
    """
    Print the value 'Hello, World!'.
    """
    print("Hello, World!")


# Challenge 4: Now its your turn!
#--------------------------------------------------
@koan
def challenge_04():
    """
    Print the value 'Python!'.

    Hint:
        Look at the previous challenge.
    """
    print("Python!")



# Challenge 5
#--------------------------------------------------
# Now that you have the hang of returning a value, let's do some simple math.
#
# Some challenges will provide you with a set of variables to start with.
# These variables are found within the parentheses of the challenge.
#
# In this challenge, you are provided with two integers.
# You task is to return the sum of two integers.
def challenge_05(integer_a, integer_b):
    """
    Return the sum of `integer_a` and `integer_b`.
    """
    return integer_a + integer_b


# Challenge 6: Now its your turn!
#--------------------------------------------------
@koan
def challenge_06(integer_a, integer_b):
    """
    Return the difference between `integer_a` and `integer_b`.

    Give it a try yourself by returning the correct value.

    Hint:
        Look at the previous challenge.
    """
    return integer_a - integer_b
