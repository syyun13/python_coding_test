# Level 3 Coding Challenge:
# Some areas were flooded by rain and you have to go to school only through the areas that are not flooded.
# The way from home to school is represented as a grid with a size of m x n.
# Home is at (1,1) and the school is at (m, n).
# 'puddles' is an array of positions of the flooded areas.
# Number of puddles are 0 to 10 and school will be never flooded.
# Find the number of shortest route you can take to go to school.
# Return the remainder after dividing it with 1000000007.

def solution(m, n, puddles):
    paths = [[0] * m for _ in range(n)]
    paths[0][0] = 1

    for row in range(n):
        for col in range(m):
            if [col + 1, row + 1] in puddles:
                paths[row][col] = 0
            else:
                if paths[row - 1][col] > 0:
                    paths[row][col] += paths[row - 1][col]
                if paths[row][col - 1] > 0:
                    paths[row][col] += paths[row][col - 1]

    return paths[-1][-1] % 1000000007
