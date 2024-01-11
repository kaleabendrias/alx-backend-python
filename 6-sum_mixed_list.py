#!/usr/bin/env python3
"""sum_mixed_list which takes a list mxd_lst"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns their sum as a float."""
    a: float = 0.0
    for x in mxd_lst:
        a += x
    return a
