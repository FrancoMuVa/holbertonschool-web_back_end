#!/usr/bin/env python3
"""
    Type-annotated function sum_mixed_list which takes a list mxd_lst of
    integers and floats and returns their sum as a float.
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Returns the sum of all numbers in mxd_lst """
    sum_num: float = 0
    for n in mxd_lst:
        sum_num += n
    return sum_num
