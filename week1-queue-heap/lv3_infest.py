# Level 3 Coding challenge:
# There is a room with a size of m x n.
# There is an infected person who can spread the disease to anyone who is only one space up/down/right/left.
# Vaccinated person will not be infected even if he/she is next to the infected person.
# 'infests' is an array of positions where infected people are at.
# 'vaccinateds' is an array of positions where vaccinated people are at.
# Return how many days it will take for everyone except the vaccinated will be infected.
# Return -1 if it is impossible for everyone except the vaccinated to get infected.

from collections import deque
def solution(m, n, infests, vaccinateds):
    answer = 0
    total = m * n
    start = len(infests) + len(vaccinateds)

    if total == start:
        return 0

    checked = [[False] * n for _ in range(m)]

    q = deque([])

    for infest_row, infest_col in infests:
        checked[infest_row - 1][infest_col - 1] = True
        q.append([infest_row - 1, infest_col - 1, 0])

    for vacc_row, vacc_col in vaccinateds:
        checked[vacc_row - 1][vacc_col - 1] = True

    infect_count = 0

    while len(q) > 0 and start + infect_count < total:
        r, c, day = q.popleft()
        paths = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for add_r, add_c in paths:
            new_r = add_r + r
            new_c = add_c + c
            if 0 <= new_r < m and 0 <= new_c < n and not checked[new_r][new_c]:
                checked[new_r][new_c] = True
                infect_count += 1
                q.append([new_r, new_c, day + 1])
                answer = day + 1

    if infect_count == 0:
        return -1

    if not start + infect_count == total:
        return -1

    return answer
