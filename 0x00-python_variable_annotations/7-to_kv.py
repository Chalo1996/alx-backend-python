#!/usr/bin/env python3
"""7-to_kv."""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    to_kv: Variable arguments.

    Args:
        k (str): first argument.
        v (int | float): second argument.

    Returns:
        tuple: returned type containing variables k and v.
    """

    sq_v: float = (v * v)

    return tuple([k, sq_v])
