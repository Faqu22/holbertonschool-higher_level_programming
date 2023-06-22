#!/usr/bin/python3
""" 6-base_geometry.py Module"""


class BaseGeometry:
    """class BaseGeometry"""
    def area(self):
        """Method what raised the exc with an msg"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method that validates a value is or not is a int"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """class Rectangle"""
    def __init__(self, width, height):
        """Method init"""
        self.integer_validator("width", width)
        self.integer_validator("heigth", height)
        self.__width = width
        self.__height = height
