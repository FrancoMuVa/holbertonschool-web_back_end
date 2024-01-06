#!/usr/bin/env python3
"""
    async routine called wait_n that takes in 2 int arguments n and max_delay.
    spawn wait_random n times with the specified max_delay.
"""
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_deley: int) -> List[float]:
    """ Returns the list of all the delays in ascending order """
    deleys: List[float] = []
    for _ in range(n):
        num = await wait_random(max_deley)
        deleys.append(num)

    sorted_deleys: List[float] = []
    for _ in range(n):
        min_deley = min(deleys)
        sorted_deleys.append(min_deley)
        deleys.remove(min_deley)

    return sorted_deleys
