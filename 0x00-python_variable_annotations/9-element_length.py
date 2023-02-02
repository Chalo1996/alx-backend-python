#!/usr/bin/env python3
"""9-element_length."""


from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    element_length: A function that return values with the appropriate types.

    Args:
        lst (List[]): _description_

    Returns:
        _type_: _description_
    """
    return [(i, len(i)) for i in lst]
