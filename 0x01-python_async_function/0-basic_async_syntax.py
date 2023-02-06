#!/usr/bin/env python3
"""0-basic_async_syntax."""


import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    wait_random: create a coroutine that returns a random time(float)\
        in seconds.

    Args:
        max_delay (int, optional): The arg. Defaults to 10.

    Returns:
        float: random time for which the coroutine will be executed.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
