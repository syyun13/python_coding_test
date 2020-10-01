# Level 2 Coding Challenge:
# Mobile board game has a game board in one straight line and three special dice.
# Each dice is made of numbers from 1 to S1, S2, S3.
# User will roll all three dice at once and move the character as much as the sum of all dice.
# 'monster' is an array of positions of the monsters. (user starts at 1)
# S1, S2, S3 is the maximum number possible for each dice.
# Return the probability that the user will not meet a monster after rolling three dice for only one time.
# (Multiply 1000 to the probability and ignore the decimals)

from itertools import product
def solution(monster, S1, S2, S3):    
    s1 = range(1, S1 + 1)
    s2 = range(1, S2 + 1)
    s3 = range(1, S3 + 1)
    outcomes = [1 + sum(outcome) for outcome in list( product(s1, s2, s3))]

    total = len(outcomes)
    no_monster = total

    for outcome in outcomes:
        if outcome in monster:
            no_monster -= 1

    return int((no_monster / total) * 1000)
