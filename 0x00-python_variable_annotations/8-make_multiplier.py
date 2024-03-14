#!/usr/bin/env python3
'''Function that applies specified multiplier to its input.
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''value to multiply.
    '''
    return lambda x: x * multiplier
