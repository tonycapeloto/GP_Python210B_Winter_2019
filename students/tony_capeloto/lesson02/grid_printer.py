# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 08:37:11 2019

@author: Tony
"""



# Part 1 copy the displayed grid using a function
# Use a for loop to start layering each line
# This line orders the creation of two rows with '+' and '-' symbols
for n in range(2):
    print('+' + ' -' * 4 + ' +' + ' -' * 4 + ' +')
    # In between and after the two rows (in range(2)), place 4 '|' symbols under each '+' sign
    for row in range(4):
        print('|' + ' ' * 8 + ' |' + ' ' * 8 + ' |')
# print the last line of the box
print('+' + ' -' * 4 + ' +' + ' -' * 4 + ' +')


# Part 2
# This function creates grids of different dimensions based on the function's input 'x'
def print_grid(x):
    # 'x' must be greater than or equal to 1
    if x <= 0:
        print('Please choose a positive number')
    # 'x' must also be divisible by 2. If it isn't, the function automatically subtracts 1 from 'x'
    if x % 2 != 0:
        x -= 1
        # 'y' is then created with a value of 'x' or 'x' - 1 divided by 2
        # this defines how many '-' and '|' symbols we are going to use in the grid
        y = x // 2
        # This line orders the creation of two rows with '+' and '-' symbols
        for n in range(2):
            print('+' + ' -' * y + ' +' + ' -' * y + ' +')
            # In between and after the two rows (in range(2)), place 'y' * '|' symbols under each '+' sign
            for row in range(y):
                print('|' + '  ' * y + ' |' + '  ' * y + ' |')
        # print the last line of the box with 'y' number of '-' symbols between the '+' symbols
        print('+' + ' -' * y + ' +' + ' -' * y + ' +')

# Part 3
# print_grid2 is a function that will take two inputs
# 'a' determines the dimension of the grid for example a = 3 will produce a 3x3 grid
# 'b' tells us how many spaces to create in between our corners
def print_grid2(a, b):
    # if 'a' or 'b' is equal to zero, the function will ask for different positive numbers
    if a <= 0 or b <= 0:
        print('Please choose two positive numbers')
    else:
        # for all other cases, we create 'a' number of border rows
        # each of the border rows has 'b' number of '-' symbols between '+' symbols
        for i in range(a):
            for i in range(a):
                print('+' + ' -' * b, end = ' ')
            print('+')
            # in between and after the 'a' number of border rows defined above, we place 'b' number of '|' symbols under each '+'
            for i in range(b):
                for i in range(a):
                    print('|' + '  ' * b, end = ' ')
                print('|')
        # the final part of the function adds a final row that duplicates the top line
        for i in range(a):
            print('+' + ' -' * b, end = ' ')
        print('+')



