#!/usr/bin/env python3
'''10 random numbers gathered using async comprehension.
'''
from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''Ten random integers listed.
    '''
    return [num async for num in async_generator()]
