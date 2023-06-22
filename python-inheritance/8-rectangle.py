#!/usr/bin/python3
""" 8-rectangle Module"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle"""
    def __init__(self, width, height):
        """Method init"""
        self.integer_validator(width)
        self.integer_validator(height)
        self.__width = width
        self.__height = height
