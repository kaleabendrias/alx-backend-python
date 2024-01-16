#!/usr/bin/env python3
"""The coroutine will loop 10 times, each time asynchronously wait 1 second"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """coroutine will loop 10 times, and yields random num"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
