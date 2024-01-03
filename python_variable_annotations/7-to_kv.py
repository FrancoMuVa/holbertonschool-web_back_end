#!/usr/bin/env python3
"""
    Type-annotated function to_kv that takes a string k and an int OR
    float v as arguments and returns a tuple.
"""


def to_kv(k: str, v: int | float) -> tuple[str, float]:
    """ returns a tuple """
    my_tuple: tuple[str, float] = (k, v ** 2)
    return my_tuple
