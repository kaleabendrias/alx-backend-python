#!/usr/bin/env python3

import asyncio
from typing import List
from random import random


async def wait_random(max_delay: int) -> float:
    """async routine that takes in an integer argument (max_delay)"""
    return random() * max_delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """spawn wait_random n times with the specified max_delay."""
    coroutines = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*coroutines)
    return delays
