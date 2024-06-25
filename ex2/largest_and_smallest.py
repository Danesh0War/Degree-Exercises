#################################################################
# FILE : calculate_mathematical_expression.py
# WRITER : daniel_riazanov , daniel.rez , 336119300
# EXERCISE : intro2cs ex2 2024
# DESCRIPTION: Module for finding the largest and smallest numbers among three given numbers
# (without math.min or math.max) as well as 5 test cases
# STUDENTS I DISCUSSED THE EXERCISE WITH: None
# WEB PAGES I USED: None
# NOTES: Why fourth case: unchecked scenario (Negative numbers)
#        Why fifth case: critical scenario (Same numbers, each equals zero)
#################################################################

def largest_and_smallest(num1, num2, num3):
    """func receives 3 numbers and returns the largest and smallest numbers. We suppose the input is correct and do
    not depend on sort max, max, min"""
    max1 = 1 / 2 * (num1 + num2 + abs(num1 - num2))
    final_max = 1 / 2 * (max1 + num3 + abs(max1 - num3))

    min1 = 1 / 2 * (num1 + num2 - abs(num1 - num2))
    final_min = 1 / 2 * (min1 + num3 - abs(min1 - num3))

    return final_max, final_min


def check_largest_and_smallest():
    first_check = (17, 1) == largest_and_smallest(17, 1, 6)
    second_check = (17, 1) == largest_and_smallest(1, 17, 6)
    third_check = (2, 1) == largest_and_smallest(1, 1, 2)
    fourth_check = (-1, -5) == largest_and_smallest(-1, -5, -3)
    fifth_check = (0, 0) == largest_and_smallest(0, 0, 0)

    is_passed = first_check and second_check and third_check and fourth_check and fifth_check
    return is_passed

