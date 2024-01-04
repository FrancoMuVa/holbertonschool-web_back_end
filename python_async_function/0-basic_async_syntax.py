#!/usr/bin/env python3
"""
    Asynchronous coroutine that takes in an integer argument
    named wait_random that waits for a random delay between 0 and max_delay
    seconds and eventually returns it.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
        Waits for a random delay between 0 and max_delay seconds
        and eventually returns it.
    """
    await asyncio.sleep(x := random.uniform(0, max_delay))
    return x
