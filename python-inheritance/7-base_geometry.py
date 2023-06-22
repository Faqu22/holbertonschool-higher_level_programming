#!/usr/bin/python3
""" 6-base_geometry.py Module"""


class BaseGeometry:
    """class BaseGeometry"""
    def area(self):
        """Method what raised the exc with an msg"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
