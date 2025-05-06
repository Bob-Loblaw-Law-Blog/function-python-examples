# Functions from Lesson 03_04
def add(x, y):
    """
    Adds two numbers.
    
    Args:
        x (int): First number
        y (int): Second number
        
    Returns:
        int: The sum of x and y
    """
    return x + y

def create_multiplier(a):
    """
    Creates a function that multiplies its input by the given value.
    
    Args:
        a (int): The multiplier
        
    Returns:
        function: A function that multiplies its input by a
    """
    return lambda x: x * a

def double_list_lambda(numbers_list):
    """
    Doubles each number in the input list using a lambda.
    
    Args:
        numbers_list (list): List of numbers
        
    Returns:
        list: A new list with each number doubled
    """
    return list(map(lambda x: x * 2, numbers_list))
