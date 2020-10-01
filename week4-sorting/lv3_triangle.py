# Level 3 Coding Challenge
# There is a triangle only made of integers.
# Find a path where the sum of all integers in the route is the largest.
# You move from top to bottom and you can only move one space down to the left or right number.
#     7
#   3   8
# 8   1   0
# In this case, you can only move down to 8 or 1 from 3.
# 'triangle' is an array that represents the triangle.
# Return the largest possible sum of integers that you pass through to reach the bottom row.

def solution(triangle):
    for row in range(1, len(triangle)):
        for col in range(len(triangle[row])):
            triangle[row][col] += add(triangle, col, row)
    return max(triangle[-1])

def add(triangle, col, row):
    if col == row:
        return triangle[row - 1][col - 1]
    elif col == 0:
        return triangle[row - 1][col]
    else:
        return max(triangle[row - 1][col - 1], triangle[row - 1][col])
