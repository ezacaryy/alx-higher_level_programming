#!/usr/bin/python3
"""class Rectangle and subclass Square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """subclass Square"""
    def __init__(self, size):
        """initilize square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """are of the square"""
        return self.__size ** 2
