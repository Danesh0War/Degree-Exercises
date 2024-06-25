#################################################################
# FILE : math_print.py
# WRITER : daniel_riazanov , daniel.rez , 336119300
# EXERCISE : intro2cs ex1 2024
# DESCRIPTION: Practising built-in math module
# STUDENTS I DISCUSSED THE EXERCISE WITH: Me, Myself & I.
# WEB PAGES I USED: none
# NOTES: ...
#################################################################


import math


def golden_ratio():
    """Function calculates and prints approx number of golden ration"""
    print((1 + math.sqrt(5)) / 2)


def six_squared():
    """Function calculates and prints res of  6^2"""
    print(math.pow(6, 2))


def hypotenuse():
    """Function calculates and prints hypotenuse of a triangle with side length 5 and 12"""
    print(math.sqrt(math.pow(5, 2) + math.pow(12, 2)))


def pi():
    """Function calculates and prints the approx π constant value"""
    print(math.pi)


def e():
    """Function calculates and prints the approx e constant value"""
    print(math.e)




def squares_area():
    """Function calculates and returns square areas of squares with side lengths from 1 to 10 included"""
    squares = [str(int(math.pow(i, 2))) for i in range(1, 11)]
    formatted_str = ' '.join(squares)  # Join squares into a single string with spaces and add a newline character to
    # fit the test format
    print(formatted_str)


if __name__ == '__main__':
    golden_ratio()
    six_squared()
    hypotenuse()
    pi()
    e()
    squares_area()
