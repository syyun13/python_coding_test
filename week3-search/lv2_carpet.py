# Level 2 Coding Challenge:
# Leo saw a carpet that is all red in the middle and all brown for the outer border.
# Leo remembers the number of reds and browns but he doesn't remember the size of the entire carpet.
# When given the number of each color, return the width and length of the carpet in an array.
# Conditions:
# 1. 8 <= brown <= 5000
# 2. 1 <= red <= 2000000
# 3. width of the carpet is longer or equal to the height.

def solution(brown, red):
    answer = []
    red_divisors = set()

    for n in range(1, red + 1):
        if red % n == 0 and n >= red//n:
            red_divisors.add((n, red//n))

    for x, y in red_divisors:
        if 2 * (x + 2) + 2 * y == brown:
            answer.append(x + 2)
            answer.append(y + 2)
    
    return answer
