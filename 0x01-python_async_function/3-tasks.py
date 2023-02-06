#!/usr/bin/env python3
"""3-tasks."""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> object:
    """
    task_wait_random: creates a coroutine task.

    Args:
        max_delay (int): random integer of sleep.

    Returns:
        task: a coroutine task
    """
    task = asyncio.Task(wait_random(max_delay))

    return task
