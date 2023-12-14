#!/usr/bin/python3
"""Defines a class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a class square that inherits from class Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Overloading __str__ method to return [Square] (<id>)
           <x>/<y> - <size>
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute

            Args:
               *args (int): The values replacing the attributes
               **kwargs (dict): Key, Value pairs of the attributes
        """
        list_atr = ["id", "size", "x", "y"]

        if args and len(args) != 0:
            for i in range(len(args)):
                if i < len(list_atr):
                    setattr(self, list_atr[i], args[i])
                else:
                    break

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key in list_atr:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
