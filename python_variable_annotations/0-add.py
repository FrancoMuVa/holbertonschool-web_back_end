#!/usr/bin/env python3
"""
    type-annotated function add that takes a float a and a float b as
    arguments and returns their sum as a float.
"""

def add(a: float, b: float) -> float:
    """ Returns a and b sum as a float """
    sum: float = a + b
    return sum