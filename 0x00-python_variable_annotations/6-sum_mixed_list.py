#!/usr/bin/env python3
'''The list of integers.
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''calculates sum of floating-point numbers and integers.
    '''
    return float(sum(mxd_lst))
