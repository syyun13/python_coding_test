# Level 3 Coding Challenge:
# Colors drawn on n x m sized paper is given as a two dimensional array named 'image'.
# When the same color is written as the same number, we want to find how many areas are in the drawing.
# An area is number of spaces where same colors are connected up and down.
# Return the number of areas in the given image.

from collections import deque
def solution(n, m, image):
    answer = 0
    
    checked = [[False] * m for _ in range(n)]
    
    for row in range(n):
        for col in range(m):
            if not checked[row][col]:
                checked[row][col] = True
                answer += 1
                
                q = deque([[row, col]])
                img = image[row][col]

                while q:
                    r, c = q.popleft()
                    path = [[-1, 0], [1, 0], [0, -1], [0, 1]]
                    for add_r, add_c in path:
                        new_r = r + add_r
                        new_c = c + add_c
                        if 0 <= new_r < n and 0 <= new_c < m and img == image[new_r][new_c] and not checked[new_r][new_c]:
                            checked[new_r][new_c] = True
                            q.append([new_r, new_c])
                        
    return answer
