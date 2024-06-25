#################################################################
# FILE : calculate_mathematical_expression.py
# WRITER : daniel_riazanov , daniel.rez , 336119300
# EXERCISE : intro2cs ex2 2024
# DESCRIPTION: Module for quadratic equation roots calculation with and without user input handling.
# STUDENTS I DISCUSSED THE EXERCISE WITH: None
# WEB PAGES I USED: None
# NOTES: None
#################################################################


import math


def quadratic_equation(a, b, c):
    """func calculates the roots of quadratic equation. We suppose that a>0.
    If there are 2 roots => func returns both
    if there is 1 root => func return root, None
    if there are no roots => func returns None,None"""
    discriminant = (b ** 2 - 4 * a * c)
    if discriminant < 0:
        return None, None
    elif discriminant == 0:
        return - b / (2 * a), None
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2


def quadratic_equation_user_input():
    """func calculates the roots of quadratic equation depending on user's coefficients and on quadratic_equation
    func logic.
    Have basic validator on user's input if a equals 0.
    If there are 2 roots => func prints both
    if there is 1 root => func prints this root
    if there are no roots => func prints 'The equation has no solutions' """
    coefficients_input = input("Insert coefficients a, b, and c: ")
    splitted_coefficients_input = coefficients_input.split()
    a = int(splitted_coefficients_input[0])
    b = int(splitted_coefficients_input[1])
    c = int(splitted_coefficients_input[2])
    if a == 0:
        print("The parameter 'a' may not equal 0")
    else:
        root1, root2 = quadratic_equation(a, b, c)
        if root1 is None:
            print("The equation has no solutions")
        elif root2 is None:
            print(f"The equation has 1 solution: {root1}")
        else:
            print(f"The equation has 2 solutions: {root1} and {root2}")
