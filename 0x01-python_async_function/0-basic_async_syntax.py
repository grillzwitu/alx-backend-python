#!/usr/bin/env python3
"""
an asynchronous coroutine that waits for a random delay between 0 and max_delay
using the random module
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """coroutine that waits for a random delay range max_delay"""
    delay: float = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
