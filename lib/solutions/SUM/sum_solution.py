# noinspection PyShadowingBuiltins,PyUnusedLocal


def compute(x: int, y: int):
    """
    Accepts two positive int arguments and returns the sum. 
    The magnitude of both integers must be less than 100.

    :param x: first positive integer to sum
    :param y: second positive integer to sum
    
    """
    assert isinstance(x, int)
    assert isinstance(y, int)
    assert x >= 0 and y >= 0, f"Both arguemnts must bo non negative integers, not {x}, {y}"

    return x + y
