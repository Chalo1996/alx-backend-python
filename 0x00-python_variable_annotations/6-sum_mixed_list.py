#!/usr/bin/env python3
"""6-sum_mixed_list."""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """
    sum_mixed_list: Adds the values of the list.

    Args:
        mxd_lst (List[float, int]): A union list of floats and integers.

    Returns:
        float: sum of the values of the list as a float.
    """

    sum: float = 0

    for (idx, val) in enumerate(mxd_lst):
        sum += val

    return sum
