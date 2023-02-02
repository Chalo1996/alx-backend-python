#!/usr/bin/env python3
"""100-safe_first_element."""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    safe_first_element: safe first element.

    Args:
        lst (Sequence[Any]): list-like sequence.

    Returns:
        Union[Any, None]: None if not safe_first_element.
    """
    if lst:
        return lst[0]
    else:
        return None
