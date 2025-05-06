# Functions from Lesson 03_03
def is_even(x):
    """
    Checks if a number is even.
    
    Args:
        x (int): The number to check
        
    Returns:
        bool: True if the number is even, False otherwise
    """
    return x % 2 == 0

def filter_even(numbers_list):
    """
    Filters a list to only include even numbers.
    
    Args:
        numbers_list (list): List of numbers
        
    Returns:
        list: A new list containing only even numbers
    """
    return list(filter(is_even, numbers_list))
