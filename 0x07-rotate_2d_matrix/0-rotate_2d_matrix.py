#!/usr/bin/python3
"""
A module that rotates a 2D matrix clockwise by 90 degrees.
"""

def rotate_2d_matrix(matrix):
    """
    A function that rotates a 2D matrix 90 degrees clockwise.
    """
    n = len(matrix)
    each_ele = 0
    each_row = n - 1

    while each_ele < each_row:
        for i in range(each_ele, each_row):
            value_tmp = matrix[i][each_row]
            matrix[i][each_row] = matrix[each_ele][i]
            value_tmp2 = matrix[each_row][each_row + each_ele - i]
            matrix[each_row][each_row + each_ele - i] = value_tmp
            value_tmp = matrix[each_row + each_ele - i][each_ele]
            matrix[each_row + each_ele - i][each_ele] = value_tmp2
            matrix[each_ele][i] = value_tmp
        each_ele += 1
        each_row -= 1
