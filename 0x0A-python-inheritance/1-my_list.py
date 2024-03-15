#!/usr/bin/python3
"""defines mylist class"""


class MyList(list):
    """MyList class"""
    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        sorted_list = sorted(self)
        print(sorted_list)
