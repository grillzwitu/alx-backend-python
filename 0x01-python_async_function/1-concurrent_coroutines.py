#!/usr/bin/env python3
""" asynchronous coroutine waits for a random delay between 0 and max_delay """
from typing import List
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    ''' spawn n times wait_random and returns List'''
    delayList = []
    finalSpawnList = []
    for x in range(n):
        delayList.append(wait_random(max_delay))
    for comp_proces in asyncio.as_completed(delayList):
        finalSpawnList.append(await comp_proces)
    return finalSpawnList
