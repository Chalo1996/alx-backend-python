#!/usr/bin/env python3
"""2-main."""

import asyncio
measure_time = __import__('2-measure_runtime').measure_time

n: int = 5
max_delay: int = 9


async def get_res() -> None:
    """Call measure_time asychronously."""
    print(await measure_time(n, max_delay))

asyncio.run(get_res())
