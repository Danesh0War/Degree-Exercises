#################################################################
# FILE : calculate_mathematical_expression.py
# WRITER : daniel_riazanov , daniel.rez , 336119300
# EXERCISE : intro2cs ex2 2024
# DESCRIPTION: Module for 3 shapes area calculation depending on user's choice following modular code principe
# STUDENTS I DISCUSSED THE EXERCISE WITH: None
# WEB PAGES I USED: None
# NOTES: None
#################################################################


import math


def shape_area():
    """
    Allows the user to choose a shape and calculates its area.

    Returns:
        The area of the chosen shape, or None if an invalid shape choice is made.
    """

    shape_choice = int(input("Choose shape (1=circle, 2=rectangle, 3=triangle): "))
    if shape_choice not in (1, 2, 3):
        return None
    elif shape_choice == 1:
        return circle_area()
    elif shape_choice == 2:
        return rectangle_area()
    else:
        return triangle_area()


def circle_area():
    """
        Calculates the area of a circle.

        Returns:
            The area of the circle.
    """
    radius = float(input())
    return math.pi * radius ** 2


def rectangle_area():
    """
    Calculates the area of a rectangle.

    Returns:
        The area of the rectangle.
    """
    first_side = float(input())
    second_side = float(input())
    return first_side * second_side


def triangle_area():
    """
    Calculates the area of an equilateral triangle.

    Returns:
        The area of the equilateral triangle.
    """
    side = float(input())
    return math.sqrt(3) / 4 * side ** 2

