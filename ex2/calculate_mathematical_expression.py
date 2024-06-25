#################################################################
# FILE : calculate_mathematical_expression.py
# WRITER : daniel_riazanov , daniel.rez , 336119300
# EXERCISE : intro2cs ex2 2024
# DESCRIPTION: Module for basic arithmetic calculations and parsing expressions from strings.
# STUDENTS I DISCUSSED THE EXERCISE WITH: None
# WEB PAGES I USED: None
# NOTES: None
#################################################################


def calculate_mathematical_expression(num1, num2, operator):
    """function performs 4 basic arithmetic calculations on 2 numbers.
    We suppose that input is correct ( num1 and num2 are numbers and operator is string type"""
    if operator not in ('+', '-', '*', '/'):
        return None
    else:
        if operator == '+':
            return num1 + num2
        if operator == '-':
            return num1 - num2
        if operator == '*':
            return num1 * num2
        if operator == '/':
            if num2 == 0:
                return None
            return num1 / num2

def calculate_from_string(expression):
    """function performs 4 basic arithmetic calculations on 2 numbers based on calculate_mathematical_expression
    logic . We suppose that input is in format (number operator number). Therefore this func only translates string
    to be used as input for the previous func"""
    split_expression = expression.split()
    num1 = float(split_expression[0])
    operator = split_expression[1]
    num2 = float(split_expression[2])

    return calculate_mathematical_expression(num1, num2, operator)

