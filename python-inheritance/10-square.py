#!/usr/bin/python3
""" 9-rectangle Module"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Class of the Square that inheritances an Rectangle"""
    def __init__(self, size):
        """Method init"""
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Method area"""
        return self.__size ** 2
