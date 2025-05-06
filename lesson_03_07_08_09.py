from functools import reduce

# Functions from Lessons 03_07, 03_08, and 03_09
def is_developer(employee):
    """
    Checks if an employee is a developer.
    
    Args:
        employee (dict): Employee data dictionary
        
    Returns:
        bool: True if the employee is a developer, False otherwise
    """
    return employee['job_title'] == 'developer'

developers = list(filter(is_developer))
print(developers)

# def is_not_developer(employee):
#     """
#     Checks if an employee is not a developer.
    
#     Args:
#         employee (dict): Employee data dictionary
        
#     Returns:
#         bool: True if the employee is not a developer, False otherwise
#     """
#     return employee['job_title'] != 'developer'

# def get_salary(employee):
#     """
#     Extracts the salary from an employee record.
    
#     Args:
#         employee (dict): Employee data dictionary
        
#     Returns:
#         int or float: The employee's salary
#     """
#     return employee['salary']

# def get_sum(acc, x):
#     """
#     Reducer function to add numbers.
    
#     Args:
#         acc: Accumulator
#         x: Current value
        
#     Returns:
#         Sum of accumulator and current value
#     """
#     return acc + x

# def analyze_salaries(employees):
#     """
#     Analyzes salaries, calculating average salaries for developers and non-developers.
    
#     Args:
#         employees (list): List of employee dictionaries
        
#     Returns:
#         dict: Analysis results with developer and non-developer salary statistics
#     """
#     # Check if employees list is empty
#     if not employees:
#         return {
#             "error": "No employee data provided"
#         }
    
#     # Filter developers and non-developers
#     developers = list(filter(is_developer, employees))
#     non_developers = list(filter(is_not_developer, employees))
    
#     # Get developer statistics
#     developer_stats = get_group_stats(developers, "developer")
    
#     # Get non-developer statistics
#     non_developer_stats = get_group_stats(non_developers, "non-developer")
    
#     # Return the combined results
#     return {
#         "developers": developer_stats,
#         "non_developers": non_developer_stats,
#         "total_employees": len(employees)
#     }

# def get_group_stats(employees, group_name):
#     """
#     Helper function to calculate statistics for a group of employees.
    
#     Args:
#         employees (list): List of employee dictionaries
#         group_name (str): Name of the group for labeling
        
#     Returns:
#         dict: Statistics for the employee group
#     """
#     if not employees:
#         return {
#             "count": 0,
#             "average_salary": 0,
#             "total_salary": 0
#         }
    
#     # Extract salaries
#     salaries = list(map(get_salary, employees))
    
#     # Calculate total salary
#     total_salary = reduce(get_sum, salaries, 0)
    
#     # Calculate average salary
#     average_salary = total_salary / len(salaries) if salaries else 0
    
#     # Return statistics
#     return {
#         "count": len(employees),
#         "average_salary": average_salary,
#         "total_salary": total_salary,
#         "employees": [employee['name'] for employee in employees]
#     }

# # Demonstrate list comprehension version (from 03_09)
# def analyze_salaries_list_comp(employees):
#     """
#     Analyzes salaries using list comprehension.
    
#     Args:
#         employees (list): List of employee dictionaries
        
#     Returns:
#         dict: Analysis results
#     """
#     if not employees:
#         return {
#             "error": "No employee data provided"
#         }
    
#     # Get developer and non-developer salaries using list comprehension
#     developer_salaries = [get_salary(x) for x in employees if is_developer(x)]
#     non_developer_salaries = [get_salary(x) for x in employees if is_not_developer(x)]
    
#     # Calculate statistics for developers
#     total_developer_salaries = sum(developer_salaries)
#     average_developer_salary = total_developer_salaries / len(developer_salaries) if developer_salaries else 0
    
#     # Calculate statistics for non-developers
#     total_non_developer_salaries = sum(non_developer_salaries)
#     average_non_developer_salary = total_non_developer_salaries / len(non_developer_salaries) if non_developer_salaries else 0
    
#     return {
#         "developers": {
#             "count": len(developer_salaries),
#             "average_salary": average_developer_salary,
#             "total_salary": total_developer_salaries
#         },
#         "non_developers": {
#             "count": len(non_developer_salaries),
#             "average_salary": average_non_developer_salary,
#             "total_salary": total_non_developer_salaries
#         },
#         "total_employees": len(employees)
#     }
