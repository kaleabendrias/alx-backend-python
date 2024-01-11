#!/usr/bin/env python3
"""Augment the following code with the correct duck-typed"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """not known types"""
    if lst:
        return lst[0]
    else:
        return None
