#!/usr/bin/env python3
import asyncio
import random

"""
asynchronous coroutine that takes in an integer argument (max_delay,
with a default value of 10)that waits for a random delay
between 0 and max_delay
(included and float value) seconds and eventually returns it.
"""


async def wait_random(max_delay=10):
    """ wait random """
    delay_time = random.uniform(0, max_delay)
    await asyncio.sleep(delay_time)
    return delay_time
