#!/usr/bin/env python3
"""5-sum_list."""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    sum_list: Returns the sum of the list elements.

    Args:
        input_list (list[float]): a list of float values.

    Returns:
        float: sum of the values of the list.
    """

    sum: float = 0

    for (idx, val) in enumerate(input_list):
        sum += val

    return sum
