#!/usr/bin/env python3
'''an integer or a float.
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''transforms a key and its value.
    '''
    return (k, float(v**2))
