#!/usr/bin/python3
"""Square class"""


class Square:
    """Square class"""

    def __init__(self, size=0, position=(0, 0)):
        """Init with size of square"""
        self._size = None
        self._position = None
        self.size = size
        self.position = position

    @property
    def size(self):
        return self._size

    @property
    def position(self):
        return self._position

    @size.setter
    def size(self, value):
        """Init with size of square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self._size = value

    @position.setter
    def position(self, value):
        """Init with size of square"""
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self._position = value

    def area(self):
        area = self.size * self.size
        return area

    def my_print(self):
        for x in range(0, self.position[1]):
            print()
        if self.size == 0:
            print()
        for x in range(0, self.size):
            for y in range(0, self.position[0]):
                print(" ", end="")
            for y in range(0, self.size):
                print("#", end="")
            print()
