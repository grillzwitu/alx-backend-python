#!/usr/bin/env python3
"""
coroutine that executes async_comprehension four times
in parallel using asyncio.gather.
measures and returns the total runtime.
"""
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    returns the total runtime.
    """
    startTime = time.time()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    return (time.time() - startTime)
