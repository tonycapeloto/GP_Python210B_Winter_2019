# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 10:16:02 2019

@author: Tony
"""

# fibonacci starts with 0 and 1 and adds n-2 with n-1 to form the next integer
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)
    
# lucas starts with 2 and 1 and adds n-2 with n-1 to form the next integer
def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-2) + lucas(n-1)
 
# sumseries allows the user to define the first two instances and adds n-2 with n-1 to form the next integer 
# if assigned 0 and 1, it will replicate the fibonacci function
# if assigned 2 and 1, it will replicate the lucas function
def sumseries(n, n0, n1):
    if n == 0:
        return n0
    elif n == 1:
        return n1
    else:
        return sumseries(n-2, n0, n1) + sumseries(n-1, n0, n1)
    
