# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 10:10:38 2019

@author: Tony
"""

# Set 'x' equal to 0
x = 0
# Use a while loop to count from x starting at 0 up to 99 (this will display 'x' starting at 1 and ending at 100)
while x <= 99:
    # for ever iteration, 'x' is increased by 1
    x += 1
    # print 'FizzBuzz' if 'x' is divisible by 3 and 5
    if x % 3 == 0 and x % 5 == 0:
        print('FizzBuzz')
    # print 'Fizz' if 'x' is divisible by 3 and not by 5
    elif x % 3 == 0 and x % 5 != 0:
        print('Fizz')
    # print 'Buzz' if 'x' is divisible by 5 and not by 3
    elif x % 5 == 0 and x % 3 != 0:
        print('Buzz')
    # if the number is not divisible by 3 or 5, then print the number
    else:
        print(x)