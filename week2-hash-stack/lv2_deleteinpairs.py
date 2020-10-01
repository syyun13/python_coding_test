# Level 2 Coding Challenge:
# 's' is a string only made of lower case characters.
# First, find a pair of same characters next to each other.
# Delete them both and connect the string together.
# Repeat until all the overlapping pairs are deleted.
# If every character can be deleted in pairs, return 1. If not, return 0.

def solution(s):
    char_stack = []
    
    for char in s:
        if len(char_stack) > 0 and char_stack[-1] == char:
            char_stack.pop()
        else:
            char_stack.append(char)
    
    if len(char_stack) == 0:
        return 1
    else:
        return 0
