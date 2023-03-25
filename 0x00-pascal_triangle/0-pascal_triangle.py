#!/usr/bin/python3

from math import factorial

"""
    0-pascal_triangle
"""

def pascal_triangle(n):
    """
        function that computes the pascal triangle 
    """
    emplist = []
    if (n <= 0):
        return emplist
    
    [emplist.append([]) for x in range(0, n)]
    for i,k in enumerate(emplist):
        while(len(k) != i+1):
            k.append(int(factorial(i) / (factorial(i-len(k))*factorial(len(k)))))
    
    return emplist
