#!/usr/bin/env python3
"""
    Function named index_range that takes two integer arguments
    page and page_size.
"""


def index_range(page, page_size):
    """
        Return a tuple of size two containing a start
        index and an end index
    """
    start_idx = (page - 1) * page_size
    end_idx = page * page_size
    return (start_idx, end_idx)
