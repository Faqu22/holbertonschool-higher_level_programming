#!/usr/bin/python3
"""Square class"""


class Square:
    """Square class"""

    def __init__(self, size=0):
        """Init with size of square"""
        self._size = None
        self.size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        """Init with size of square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self._size = value

    def area(self):
        area = self.size * self.size
        return area

    def my_print(self):
        if self.size == 0:
            print()
        for x in range(0, self.size):
            for y in range(0, self.size):
                print("#", end="")
            print()
