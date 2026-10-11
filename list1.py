# -*- coding: utf-8 -*-
"""
Created on Tue Oct 6 10:39:30 2026

@author: Student
"""

def divisible(numbers, divisor):
    """Return integers from numbers that are divisible by divisor.

    Args:
        numbers (list[int]): List of integers to check.
        divisor (int): Integer used to test divisibility.

    Returns:
        list[int]: Numbers from numbers that are divisible by divisor.

    Raises:
        TypeError: If numbers is not a list of integers or divisor is not
        an integer.
        ValueError: If divisor is zero.

    Preconditions:
        - numbers is a list containing only integers.
        - divisor is a non-zero integer.

    Postconditions:
        - The returned list contains only numbers from numbers that are
        divisible by divisor.
        - The order of numbers is preserved.
    """
    
    if not isinstance(numbers, list):
        raise TypeError("Numbers must be a list.")
        #checks if numbers is an instance of a list class
        
    if not all(type(number)is int for number in numbers):
        raise TypeError("Numbers must contain only integers.")
        #checks if the list numbers contains integers only
        
    if type(divisor) is not int:
        raise TypeError("A divisor must be an integer.")
        #cheks if the divisor is an integer
        
    if divisor==0:
        raise ValueError("Divisor cannot be 0.")
        #checks if a divisor is equal to 0

    result = []

    for number in numbers:
        if number % divisor == 0:
            result.append(number)

    return result

def common(x, y):
    """Return the intersection of two multisets
    
    Args:
        x( list): The first multiset.
        y (list): The second multiset.
        
    Returns:
        list: Elements common to both multisets, with each element
        appearing as many times as the minimum of its counts in x and y.
        
    Raises:
        TypeError: if x or y is not a list.
        
    Preconditions:
        - x and y are lists.
        
    Postconditions:
        - Each element occurs in the result as many times as the
        minimum of its conts in x and y
        - The order of elements follows their first occurences in x.    
    """
    
    if not isinstance(x, list) or not isinstance(y, list):
        raise TypeError("Both x and y must be lists.")
    #checks if x and y are lists
    
    result = []
    remaining = y.copy()
    
    for element in x:
        if element in remaining:
            result.append(element)
            remaining.remove(element)
            
    return result
        