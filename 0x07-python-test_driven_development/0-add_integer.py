#!/usr/bin/python3

"""An addition function that  """


def add_integer(a, b=98):
    """Takes two arguments of type integer or float and returns the sum
    of their values. If a or b are float values they are typecasted to
    integers before performing the addition.

    Args:
    a: first integer or float to be added
    b: second integer or float to be added

    Return: Sum of argument a and argument b

    Raises:
    TypeError: argument a and b must be either an integer or a float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
