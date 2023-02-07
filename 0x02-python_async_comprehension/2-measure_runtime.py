#!/usr/bin/env python3
""""2-measure_runtime module."""


import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure_runtime: Uses asyncio.gather to execute a coroutine four\
        times and calculate the total runtime of the concurrency \
            of the coroutines. Each coroutine takes the average time. \
                since async_comprehension is asynchronously executed, \
                    each random number will be generated and stored in the \
                    list at O(1) which is the asyncio.sleep time. For \
                        ten random numbers, it would be O(n) -> 10 \
                            seconds(roughly).

    Returns:
        float: The mean time of the concurrency which is equivalent \
            to the runtime of each coroutine.
    """
    start_time: float = time.time()
    await asyncio.gather(async_comprehension())
    end_time: float = time.time()

    total_time: float = end_time - start_time
    return total_time
