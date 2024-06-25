#################################################################
# FILE : calculate_mathematical_expression.py
# WRITER : daniel_riazanov , daniel.rez , 336119300
# EXERCISE : intro2cs ex2 2024
# DESCRIPTION: Module for evaluating (boolean) whether it is safe to travel to vormir based on temperature comparisons
# STUDENTS I DISCUSSED THE EXERCISE WITH: None
# WEB PAGES I USED: None
# NOTES: None
#################################################################


def is_vormir_safe(threshold_temp, first_day_temp, second_day_temp, third_day_temp):
    """
    Determines if it's safe for Thanos to travel to Vormir based on the temperature measurements.

    Parameters:
        threshold_temp (float): The threshold temperature.
        first_day_temp (float): Temperature measurement for day 1.
        first_day_temp (float): Temperature measurement for day 2.
        first_day_temp (float): Temperature measurement for day 3.

    Returns:
        bool: True if at least two out of the three days have temperatures higher than the threshold, False otherwise.
    """
    is_above_on_day1 = first_day_temp > threshold_temp
    is_above_on_day2 = second_day_temp > threshold_temp
    is_above_on_day3 = third_day_temp > threshold_temp

    count = int(is_above_on_day1) + int(is_above_on_day2) + int(is_above_on_day3)

    return count >= 2
