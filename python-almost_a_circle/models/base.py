#!/usr/bin/python3
"""this is a base class."""
import json
import csv
import turtle


class Base:
    """The base class."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization method."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
