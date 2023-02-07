#!/usr/bin/env python3
"""0-async_generator."""

import random
import asyncio
from typing import Iterator


async def async_generator() -> Iterator[float]:
    """
    async_generator: Generates a generator of integers.

    Yields:
        Generator[int, None, None]: A random number through every loop.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
