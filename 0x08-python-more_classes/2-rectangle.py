#!/usr/bin/python3
"""Calculate the area of a rectangle"""

class Rectangle:
    """Define the rectangle"""

    def __init__(self, width=0, heigth=0):
        """"Initilaize the rectangle.
        Args:
            heigth (int): height of the rectangle
            width (int): width of the rectangle
        """
        self.width = width
        self.heigth = heigth

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
    def heigth(self):
        """defines a height"""
        return self.__heigth

    @heigth(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("heigth must be >= 0")

    def area(self):
        """calculates the area"""
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.width == 0:
            return 0

        """calcualte the perimeter"""
        return (self.__heigth * 2) + (self.__width * 2)

