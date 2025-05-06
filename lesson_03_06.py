from functools import reduce

# Functions from Lesson 03_06
def get_sum(acc, x):
    """
    Reducer function that adds an element to an accumulator.
    
    Args:
        acc: The accumulator
        x: The current value
        
    Returns:
        The updated accumulator
    """
    return acc + x

def get_sum_reduce(numbers_list):
    """
    Computes the sum of all numbers in the list using reduce.
    
    Args:
        numbers_list (list): List of numbers
        
    Returns:
        int or float: The sum of all numbers in the list
    """
    if not numbers_list:
        return 0
    return reduce(get_sum, numbers_list)
