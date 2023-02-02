#!/usr/bin/env python3
"""8-make_multiplier."""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    make_multiplier:

    Args:
        multiplier (float): argument.

    Returns:
        Callable[float]: function that multiplies a float by multiplier.
    """
    def get_multiplier(x: float) -> float:
        """
        get_multiplier: function that multiplies a float by multiplier.

        Args:
            x (float): value to multiply by.

        Returns:
            float: The Callable return value.
        """
        return x * multiplier
    return get_multiplier
