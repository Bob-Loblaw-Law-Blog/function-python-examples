# Functions from Lesson 03_05
def double_list_comp(numbers_list):
    """
    Doubles each number in the input list using list comprehension.
    
    Args:
        numbers_list (list): List of numbers
        
    Returns:
        list: A new list with each number doubled
    """
    return [x * 2 for x in numbers_list]

def filter_even_list_comp(numbers_list):
    """
    Filters a list to only include even numbers using list comprehension.
    
    Args:
        numbers_list (list): List of numbers
        
    Returns:
        list: A new list containing only even numbers
    """
    return [x for x in numbers_list if x % 2 == 0]
