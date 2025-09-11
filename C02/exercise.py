"""
Welcome to koan exercise 2.

Please provide a solution for each coding challenge.
"""

data = {
    "Foo": "Bar"
}


# Challenge 1
#--------------------------------------------------
def challenge_01(a, b):
    """Return the sum of a and b using arithmetic operators."""
    raise NotImplementedError()


# Challenge 2
#--------------------------------------------------
def challenge_02(a, b):
    """Return True if a is greater than b, else False (comparison operator)."""
    raise NotImplementedError()


# Challenge 3
#--------------------------------------------------
def challenge_03(x, y):
    """Return True only if both x and y are True (logical operator)."""
    raise NotImplementedError()


# Challenge 4
#--------------------------------------------------
def challenge_04(n):
    """Assign n to a variable, increment it by 1 using assignment operator, and return the result."""
    raise NotImplementedError()


# Challenge 5
#--------------------------------------------------
def challenge_05(number):
    """
    Return a `list` of strings for numbers from 1 to `number`:
        - `FizzBuzz` if divisible by 3 and 5,
        - `Fizz` if divisible by 3,
        - `Buzz` if divisible by 5,
        - else the `number` as a string.

    Hint:
        Uses a `for` loop and conditional statements.
    """
    result = []
    for index in range(1, number + 1):
        if index % 3 == 0 and index % 5 == 0:
            result.append('FizzBuzz')
        elif index % 3 == 0:
            result.append('Fizz')
        elif index % 5 == 0:
            result.append('Buzz')
        else:
            result.append(str(index))
    raise NotImplementedError()


# Challenge 6
#--------------------------------------------------
def challenge_06(start):
    """
    Return a list counting down from start to 1 using a while loop.
    """
    raise NotImplementedError()


# Challenge 7
#--------------------------------------------------
def challenge_07(score):
    """
    Return a message based on `score`:
    - `Excellent` if score >= 90
    - `Good` if score >= 75
    - `Pass` if score >= 60
    - `Fail` otherwise

    Returns:
        str: The message corresponding to the score.

    Hint:
        Uses the `if`, `elif`, and `else` conditional statements.
    """
    raise NotImplementedError()
