"""
Routines for geometric calculations
"""
from math import pi

def circle_area(diameter):
    """
    Calculate area of a circle with given diameter

    """
    return pi * ((diameter / 2) ** 2)

def rectangle_area(length, width):
    """
    Calculate area of a rectangle

    :param length: length of longer side
    :param width: length of shorter side
    :return: area
    """
    return length * width

def square_area(length):
    return rectangle_area(length, length)

def _spam():  # "private"
    print("spam spam spam")

