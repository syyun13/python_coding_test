# Level 2 Coding Challenge:
# When given 0 or positive integers, find the largest number you can make by connecting those numbers.
# For example, if [6, 10, 2] is given, the largest number you can make is 6210.
# 'numbers' is an array of integers from 0 to 1000.
# Return the value as string.

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(reverse=True, key=triple)

    if numbers[0] == "0" and numbers[-1] == "0":
        return "0"
    else:
        return "".join(numbers)

def triple(x):
    return x * 3
