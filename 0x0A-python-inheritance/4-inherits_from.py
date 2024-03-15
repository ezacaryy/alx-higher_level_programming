#!/usr/bin/python3
"""inherits_from function"""


def inherits_from(obj, a_class):
    """true if obj is a subclass of a class, otherwise false"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
