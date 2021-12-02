#!/usr/bin/env python3
"""A function using type annotation"""
from typing import List, Sequence, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Returns a list of a tuple'''
    return [(i, len(i)) for i in lst]
