#!/usr/bin/env python3
"""3-tasks."""

import asyncio
from typing import Callable

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Callable[[None], float]:
    """
    task_wait_random: creates a coroutine task.

    Args:
        max_delay (int): random integer of sleep.

    Returns:
        task: a coroutine task
    """

    def innerFunc():
        return asyncio.create_task(wait_random(max_delay))

    return innerFunc()
