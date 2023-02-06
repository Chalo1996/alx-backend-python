#!/usr/bin/env python3
"""2-measure_runtime."""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measure_time: calculate the totoal time taken to asynchronously \
        call wait_n n times.

    Args:
        n (int): number of times n is called.
        max_delay (int): range of generation of random delay.

    Returns:
        float: total time taken for wait_n to return.
    """
    start_time = time.time()
    wait_n(n, max_delay)
    end_time = time.time()

    total_time = end_time - start_time

    return total_time / n
