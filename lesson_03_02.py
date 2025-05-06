# Function from Lesson 03_02
def double(x):
    """
    Doubles the input value.
    
    Args:
        x (int): The number to double
        
    Returns:
        int: The doubled value
    """
    return x * 2

# Function to demonstrate map functionality
def double_list(numbers_list):
    """
    Doubles each number in the input list.
    
    Args:
        numbers_list (list): List of numbers
        
    Returns:
        list: A new list with each number doubled
    """
    return list(map(double, numbers_list))
