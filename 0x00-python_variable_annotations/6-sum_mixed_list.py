#!/usr/bin/env python3
"""A function using type annotation"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    '''Returns the sum of the elements in the mxd_lst'''
    return sum(mxd_lst)
