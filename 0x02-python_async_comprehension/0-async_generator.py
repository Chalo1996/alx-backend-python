#!/usr/bin/env python3
"""0-async_generator module."""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    async_generator: Generates a generator of integers.

    Args:
        None.

    Yields:
        Generator[float, None, None]: A random float number through every\
            loop. Waits for one minute before generating the next random float.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
