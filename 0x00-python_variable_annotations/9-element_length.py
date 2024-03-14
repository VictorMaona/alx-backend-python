#!/usr/bin/env python3
'''calculates a list of sequences length.
'''
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''list of tuples containing each sequence.
    '''
    return [(i, len(i)) for i in lst]
