#!/usr/bin/env python3
"""3-tasks."""

import asyncio
from typing import Awaitable

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: float) -> Awaitable[float]:
    """
    task_wait_random: creates a coroutine task.

    Args:
        max_delay (int): random integer of sleep.

    Returns:
        task: a coroutine task
    """

    return (asyncio.create_task(wait_random(max_delay)))
