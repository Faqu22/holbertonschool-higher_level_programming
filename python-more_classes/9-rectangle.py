#!/usr/bin/python3
"""Rectangle"""


class Rectangle:
    """Rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height != 0 and self.__width != 0:
            return (self.__width * 2) + (self.__height * 2)
        else:
            return 0

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    def __str__(self):
        if self.__width == 0 or self.height == 0:
            return ''

        for i in range(self.__height - 1):
            print(str(self.print_symbol) * self.__width)
        print(str(self.print_symbol) * self.__width, end="")
        return ''

    def __repr__(self):
        return f"{self.name}({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    """
        @classmethod:
        Is a decorator in Python used to define a method that belongs to
        the class rather than an instance of the class. It receives the class
        itself as the first argument, commonly referred to as cls, instead of
        the instance (self). Class methods are useful when you need to perform
        operations or access class-level attributes without requiring an
        instance.
    """
    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)
