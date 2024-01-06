#!/usr/bin/env python3
"""
    async routine called wait_n that takes in 2 int arguments n and max_delay.
    spawn wait_random n times with the specified max_delay.
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_deley: int) -> list[float]:
    """ Returns the list of all the delays in ascending order """
    deleys: list = [wait_random(max_deley) for _ in range(n)]
    all_deleys: list = await asyncio.gather(*deleys)
    sorted_deleys: list[float] = []
    for _ in range(n):
        min_deley = min(all_deleys)
        sorted_deleys.append(min_deley)
        all_deleys.remove(min_deley)
    return sorted_deleys
