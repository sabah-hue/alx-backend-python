#!/usr/bin/env python3
"""
takes an integer max_delay and returns a asyncio.Task.
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(n, max_delay):
    """ wait random n times """
    tasks = [wait_random(max_delay) for _ in range(n)]
    tasks = asyncio.as_completed(tasks)
    arr = []
    for i in tasks:
        x = await i
        arr.append(x)
    return arr
