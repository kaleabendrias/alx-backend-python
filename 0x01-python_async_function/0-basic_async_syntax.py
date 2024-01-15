#!/usr/bin/env python3
"""Basic Async Syntax"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """async routine that takes in an integer argument (max_delay)"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
