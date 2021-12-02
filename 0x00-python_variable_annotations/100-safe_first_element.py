#!/usr/bin/env python3
"""A function using Duck-typed annotations"""
from typing import Union, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''Returns any if lst or none'''
    if lst:
        return lst[0]
    else:
        return None
