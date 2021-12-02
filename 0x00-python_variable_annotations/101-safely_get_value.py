#!/usr/bin/env python3
"""A function using Duck-typed annotations"""
from typing import Union, Mapping, Any, TypeVar

T = TypeVar("T")


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None
                     ) -> Union[Any, T]:
    '''correct duck-typed annotations'''
    if key in dct:
        return dct[key]
    else:
        return default
