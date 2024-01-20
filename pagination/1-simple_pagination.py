#!/usr/bin/env python3
"""
    Function named index_range that takes two integer arguments
    page and page_size.
"""
import csv
import math
from typing import List


def index_range(page, page_size):
    """
        Return a tuple of size two containing a start
        index and an end index
    """
    start_idx = (page - 1) * page_size
    end_idx = page * page_size
    return (start_idx, end_idx)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Get page """
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        idx_range = index_range(page, page_size)
        dataset_len = len(self.dataset())
        if idx_range[0] >= dataset_len:
            return []
        return self.dataset()[idx_range[0]:idx_range[1]]
