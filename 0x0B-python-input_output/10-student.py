#!/usr/bin/python3
"""
contains the class student
"""


class Student:
    """Represents a student"""
    def __init__(self, first_name, last_name, age):
        """Initialise a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns the dict representation of a student"""
        return self.__dict__

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.
        If attrs is a list of strings, represents only those attributes
        included in the list.
        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if type(attrs) is list and all(type(elt) for elt in attrs):
            return {item: getattr(self, item) for
                    item in attrs if hasattr(self, item)}
        return self.__dict__
