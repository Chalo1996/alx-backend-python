#!/usr/bin/env python3
"""1-concurrent_coroutines."""

import asyncio

from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    wait_n: A routine that calls another routine repeatedly.

    Args:
        n (int): number of times to call wait_random.
        max_delay (int): range of values generated by wait_random every time \
            it is called.

    Returns:
        List[float]: A list of sorted floats returned for every routine call.
    """
    delaysLst: list = list()
    for i in range(n):
        delaysLst.append((await wait_random(max_delay)))

    return sorted(delaysLst)
