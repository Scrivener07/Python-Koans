"""
Provides features that support Python koans.
"""

def koan(function):
    """
    This function decorator marks a function as a koan challenge.
    These koan functions are stubbed during the `publish.py` post processing.
    """
    function._koan = True
    return function
