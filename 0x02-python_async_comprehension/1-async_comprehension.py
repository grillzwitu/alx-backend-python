#!/usr/bin/env python3
"""
coroutine called async_comprehension that takes no arguments.
It collects 10 random numbers,
using an async comprehensing over async_generator,
then returns the 10 random numbers.
"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    collects 10 random numbers using an async comprehensing
    over async_generator, then returns the 10 random numbers.
    """
    return [x async for x in async_generator()]
