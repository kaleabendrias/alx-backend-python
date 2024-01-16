#!/usr/bin/env python3
"""write a coroutine called async_comprehension"""


import asyncio
import random
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> float:
    """collect 10 random numbers using an async comprehensing"""
    return [i async for i in async_generator()]
