#!/usr/bin/python3
'''module derives a pascal triangle up to a given number'''


def pascal_triangle(n):
    '''creates and return a nested list that make up a pascal triangle up to ni
    Args:
        n(int): number of levels for the pascal triangle
    Return:
        matrix: list of list that defines a pascal triangle of n levels
    '''
    triangle = []
    if n <= 0:
        return triangle

    triangle.append([1])
    for i in range(n - 1):
        curr_level = [1]
        for j in range(len(triangle[i])):
            if j < len(triangle[i]) - 1:
                curr_sum = triangle[i][j] + triangle[i][j+1]
                curr_level.append(curr_sum)
        curr_level.append(1)
        triangle.append(curr_level)
    return triangle
