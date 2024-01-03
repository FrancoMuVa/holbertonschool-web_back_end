#!/usr/bin/env python3
"""
    Type-annotated function sum_list which takes a list input_list of
    floats as argument and returns their sum as a float.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Returns the sum of all floats in input_list """
    sum_float: float = 0
    for n in input_list:
        sum_float += n
    return sum_float
