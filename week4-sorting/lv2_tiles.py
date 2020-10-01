# Level 2 Coding Challenge:
# There is a rectangular tile with width 2 and height 1.
# With these tiles, you want to cover the entire floor with width n and height 2.
# Find a number of combinations you can place the tile to fill the floor.
# Since the number can be extremely large, divide it by 1000000007 and return the remainder.

def solution(n):
    tiles = [1, 2]

    for _ in range(2, n):
        tiles.append((tiles[-2] + tiles[-1]) % 1000000007)

    return tiles[-1]
