# Level 2 Coding Challenge:
# 'nums' is an array of integers from 1 to 1000 with no repeats.
# Return the number of combinations where the sum of three numbers is a prime number.

from itertools import combinations
def solution(nums):
    return len(list(filter(isPrime, [sum(combination) for combination in combinations(nums, 3)])))

def isPrime(num):
    if num < 2:
        return False
    for div in range(2, int(num ** 0.5 + 1)):
        if num % div == 0:
            return False
    return True
