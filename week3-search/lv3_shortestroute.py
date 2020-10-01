# Level 3 Coding Challenge:
# To win the game, you have to reach the opposing team's camp as fast as you can.
# The map has a size of n x m. 0 is a wall and 1 is not a wall.
# The character can only move one space up/down/left/right at a time to where there is no wall.
# If the opposing team's camp is surrounded with walls, you might not be able to reach it at all.
# 'maps' is an array of n x m sized game board with only 0 and 1.
# Return the smallest number of spaces you have to move to reach the opponent.
# Return -1 if it is impossible to arrive at the opposing team's camp.

from collections import deque
def solution(maps):
    m = len(maps)
    n = len(maps[0])
    visited = [ [0] * n for _ in range(m) ]
    path = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    
    q = deque([[0, 0]])
    visited[0][0] = 1

    while q:
        r, c = q.popleft()
        if r == m - 1 and c == n - 1:
            return visited[r][c]
        for add_r, add_c in path:
            new_r = r + add_r
            new_c = c + add_c
            if 0 <= new_r < m and 0 <= new_c < n and not visited[new_r][new_c] and maps[new_r][new_c]:
                visited[new_r][new_c] = visited[r][c] + 1
                q.append([new_r, new_c])

    return -1
