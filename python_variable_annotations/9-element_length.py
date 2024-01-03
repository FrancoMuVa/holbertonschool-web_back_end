#!/usr/bin/env python31
"""
    Function that returns a list of tuples.
"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Returns a list of tuples """
    return [(i, len(i)) for i in lst]
