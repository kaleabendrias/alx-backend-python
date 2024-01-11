#!/usr/bin/env python3
"""to_kv that takes a string k and an int OR float v as arguments """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns a tuple."""
    x = v ** 2
    return (k, x)
