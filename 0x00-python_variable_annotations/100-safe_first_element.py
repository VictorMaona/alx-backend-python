#!/usr/bin/env python3
'''sequence or none if sequence is empty.
'''
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''retrieves a sequence initial element if it is present.
    '''
    if lst:
        return lst[0]
    else:
        return None
