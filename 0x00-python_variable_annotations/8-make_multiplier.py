#!/usr/bin/env python3
"""A function using type annotation"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Returns a function that multiplies floats'''
    def multiplyFloat(n: float) -> float:
        '''returns multiplication'''
        return n * multiplier
    return multiplyFloat
