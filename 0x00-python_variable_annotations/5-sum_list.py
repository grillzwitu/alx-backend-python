#!/usr/bin/env python3
"""A function using type annotation"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''Returns the sum of the elements in the list of floats'''
    return sum(input_list)
