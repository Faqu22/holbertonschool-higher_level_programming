#!/usr/bin/python3
"""Task 10"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(height=size, width=size, x=x, y=y, id=id)

    @property
    def size(self):
        return self.__width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def __str__(self):
        """
        This function is called when you want to print the class
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
