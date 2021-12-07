#!/usr/bin/env python3
"""
coroutine called async_generator that takes no arguments
loop 10 times, each time asynchronously wait 1 second,
then yield a random number between 0 and 10.
"""

from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """
    loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10, using random module
    """
    for x in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
