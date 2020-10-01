# Level 3 Coding Challenge:
# Bingo has a size of n x n and it is filled with all different integers.
# 'board' is a two dimensional array of all numbers in the n x n bingo board.
# 'nums' is an array of numbers that will be checked.
# Return how many bingos are made when we check all the numbers in 'nums'.

def solution(board, nums):
    answer = 0
    n = len(board)

    bingo_board = { board[row][col]: [row, col] for row in range(n) for col in range(n) }
    row_check = { n: [] for n in range(n) }
    col_check = { n: [] for n in range(n) }
    diagonal_1 = []
    diagonal_2 = []

    for num in nums:
        r, c = bingo_board[num]
        row_check[r].append(num)
        col_check[c].append(num)
        if r == c:
            diagonal_1.append(num)
        if r + c == n - 1:
            diagonal_2.append(num)

    for _, bingo_row in row_check.items():
        if len(bingo_row) == n :
            answer += 1

    for _, bingo_col in col_check.items():
        if len(bingo_col) == n:
            answer += 1

    if len(diagonal_1) == n:
        answer += 1
    if len(diagonal_2) == n:
        answer += 1
    
    return answer
