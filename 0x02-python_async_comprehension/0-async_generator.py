#!/usr/bin/env python3
"""0-async_generator."""

import random
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[int, None]:
    """
    async_generator: Generates a generator of integers.

    Args:
        None.

    Yields:
        Generator[int, None, None]: A random number through every loop.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
