"""
Welcome to koan exercise 2.

Please provide a solution for each coding challenge.
"""
from koans import koan


# Challenge 1
#--------------------------------------------------
@koan
def challenge_01(a, b):
    """
    Return the sum of `a` and `b` using arithmetic operators. 2
    """
    return a + b


# Challenge 2
#--------------------------------------------------
@koan
def challenge_02(a, b):
    """
    Return `True` if `a` is greater than `b`, else `False` (comparison operator).
    """
    return a > b


# Challenge 3
#--------------------------------------------------
@koan
def challenge_03(x, y):
    """
    Return `True` only if both `x` and `y` are `True` (logical operator).
    """
    return x and y


# Challenge 4
#--------------------------------------------------
@koan
def challenge_04(number):
    """
    Increment the `number` variable by 1 using assignment operator, and return the result.
    """
    number += 1
    return number


# Challenge 5
#--------------------------------------------------
@koan
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
    return result


# Challenge 6
#--------------------------------------------------
@koan
def challenge_06(start):
    """
    Return a list counting down from start to 1 using a while loop.
    """
    result = []
    while start > 0:
        result.append(start)
        start -= 1
    return result


# Challenge 7
#--------------------------------------------------
@koan
def challenge_07(score):
    """
    Return a message based on the provided `score`.

    Messages:
    - `Excellent` if score >= 90
    - `Good` if score >= 75
    - `Pass` if score >= 60
    - `Fail` otherwise

    Returns:
        `str`: The message corresponding to the score.

    Hint:
        Uses the `if`, `elif`, and `else` conditional statements.
    """
    if score >= 90:
        return "Excellent"
    elif score >= 75:
        return "Good"
    elif score >= 60:
        return "Pass"
    else:
        return "Fail"


# Challenge 8
#--------------------------------------------------
@koan
def challenge_08(numbers):
    """
    Return the sum of all even numbers in the list `numbers`.

    Provided Variables:
        numbers (`list[int]`): A list of integers.

    Returns:
        `int`: The sum of all even numbers in the provided list.
    """
    total = 0
    for number in numbers:
        if number % 2 == 0:
            total += number
    return total



# Challenge 8
#--------------------------------------------------
@koan
def challenge_09(numbers):
    """
    Return the sum of all odd numbers in the list `numbers`.

    Provided Variables:
        numbers (`list[int]`): A list of integers.

    Returns:
        `int`: The sum of all odd numbers in the provided list.
    """
    total = 0
    for number in numbers:
        if number % 2 != 0:
            total += number
    return total
