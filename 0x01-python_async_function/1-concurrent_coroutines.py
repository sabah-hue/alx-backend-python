#!/usr/bin/env python3
"""
async routine called wait_n that takes in
2 int arguments (in this order): n and max_delay.
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """ wait random n times """
    tasks = [wait_random(max_delay) for _ in range(n)]
    tasks = asyncio.as_completed(tasks)
    arr = []
    for i in tasks:
        x = await i
        arr.append(x)
    return arr
