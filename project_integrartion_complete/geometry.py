"""
@file geometry.py
@brief This module contains functions to calculate area and perimeter of geometrical shapes.
"""
import math
def rectangle_area(length, width):
    """
    Calculate the area of a rectangle.
    
    @param length Length of the rectangle
    @param width Width of the rectangle
    @return Area of the rectangle
    """
    return length * width

def rectangle_perimeter(length, width):
    """
    Calculate the perimeter of a rectangle.
    
    @param length Length of the rectangle
    @param width Width of the rectangle
    @return Perimeter of the rectangle
    """
    return 2 * (length + width)

def circle_area(radius):
    """
    Calculate the area of a circle.
    
    @param radius Radius of the circle
    @return Area of the circle
    """
    return math.pi * (radius ** 2)

def circle_circumference(radius):
    """
    Calculate the circumference of a circle.
    
    @param radius Radius of the circle
    @return Circumference of the circle
    """
    return 2 * math.pi * radius
