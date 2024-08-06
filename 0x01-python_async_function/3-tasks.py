#!/usr/bin/env python3
"""
takes an integer max_delay and returns a asyncio.Task.
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """ create tasks """
    # return asyncio.Task(wait_random(max_delay))
    return asyncio.create_task(wait_random(max_delay))
