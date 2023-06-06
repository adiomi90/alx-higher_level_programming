#!/usr/bin/python3
"""Calculate the area of a rectangle"""


class Rectangle:
    """Define the rectangle"""


    def __init__(self, width=0, height=0):
        """"Initilaize the rectangle.
        Args:
            height (int): height of the rectangle
            width (int): width of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """defines the width"""
        return self.__width


    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """defines a height"""
        return self.__height


    @height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculates the area"""
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.width == 0:
            return 0

        """calcualte the perimeter"""
        return (self.__heigth * 2) + (self.__width * 2)

