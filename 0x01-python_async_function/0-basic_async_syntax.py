#!/usr/bin/env python3
'''Async module.
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''waits an arbitrary amount of time in seconds.
    '''
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
