#!/usr/bin/python3
""" 8-rectangle Module"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle"""
    def __init__(self, width, height):
        """Method init"""
        self.integer_validator("width", width)
        __width = width
        self.integer_validator("heigth", height)
        __height = height
