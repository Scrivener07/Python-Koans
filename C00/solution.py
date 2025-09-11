"""
Welcome to the getting started primer for koan challenges.

Each challenge is a labeled group of Python code lines.
Your job: Fill in the blank below each label with your answer.

You do not need to understand how these labels work yet.
Just focus on writing the correct code for each challenge.
"""
from ..koans import koan

# Challenge 1
#--------------------------------------------------
# The most common type of challenge will have you `return` a value.
# The word `return` is a special keyword in Python written as `return <value>`.
# You can think of the `return` keyword as how you submit your answer.
#
# In this first challenge, you are asked to return the string "Hello, World!".
# There is nothing to calculate, so we can just submit the string.
#
# The string "Hello, World!" here is the <value> for which you must return.
def hello_string():
    """
    Return the string 'Hello, World!'.
    """
    return "Hello, World!"


# Challenge 2: Now its your turn!
#--------------------------------------------------
@koan
def python_string():
    """
    Return the string 'Python'.
    """
    return "Python"



# Challenge 3
#--------------------------------------------------
# Sometimes a challenge won't require you to return a value at all.
#
# In this challenge you only need to `print()` the solution.
def hello_print():
    """
    Print the value 'Hello, World!'.
    """
    print("Hello, World!")


# Challenge 4: Now its your turn!
#--------------------------------------------------
@koan
def python_print():
    """
    Print the value 'Python!'.
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
def add_two_numbers(integer_a, integer_b):
    """
    Return the sum of `integer_a` and `integer_b`.
    """
    return integer_a + integer_b


# Challenge 6: Now its your turn!
#--------------------------------------------------
@koan
def subtract_two_numbers(integer_a, integer_b):
    """
    Return the difference between `integer_a` and `integer_b`.

    Give it a try yourself by returning the correct value.

    Hint:
        Look at the previous challenge.
    """
    return integer_a - integer_b
