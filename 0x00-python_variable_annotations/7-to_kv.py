#!/usr/bin/env python3
"""A function using type annotation"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[float, int]) -> Tuple[str, float]:
    '''Returns a tuple with a string and a float'''
    return k, v**2
