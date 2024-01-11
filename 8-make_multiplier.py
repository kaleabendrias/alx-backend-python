#!/usr/bin/env python3
"""make_multiplier that takes a float multiplier as argument """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """make_multiplier that takes a float multiplier as argument """
    return lambda x: x * multiplier
