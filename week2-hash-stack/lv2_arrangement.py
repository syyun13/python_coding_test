# Level 2 Coding Challenge:
# You are trying to cut several bars of iron with a laser.
# For efficiency, iron bars are laid from bottom to top and lasers are fired vertically from the top.
# The placement of iron bars and lasers should follow 4 conditions.
# 1. An iron bar can only be placed on top of another iron bar that is longer.
# 2. If an iron bar is palced on top of another one, it should be placed fully inclusive without the end points overlapping.
# 3. At least one laser exists to cut each bar.
# 4. The laser does not overlap with any iron bar's end points.
# A laser is written as a closed parenthesis '()' without anything inside.
# Left end of an iron bar is written as '(', right end of an iron bar is written as ')'.
# 'arrangement' is a string that expresses the placement of iron bars and lasers.
# Return the total number of iron bar fragments that were cut.

def solution(arrangement):
    answer = 0

    arrangement = arrangement.replace("()", "X")

    left_count = 0

    for el in arrangement:
        if el == "X":
            answer += left_count
        if el == "(":
            left_count += 1
        if el == ")":
            left_count -= 1
            answer += 1
    
    return answer
