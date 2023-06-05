#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    """Represents a rectangle"""

    def __init__(self, width, height):
        """Initializes the current rectangle.
         Args:
            height (int): height of the rectangle
            width (int): width of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Defines a width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) !=  int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Defines the height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
