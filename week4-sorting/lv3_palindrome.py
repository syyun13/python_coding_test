# Level 3 Coding Challenge:
# When given string s, find the longest palindrome from all the possible substrings
# and return the length of that palindrome.
# Maximum possible length of s is 2500 and only lower case alphabets are used.

def solution(s):
    answer = 0

    for start in range(len(s) + 1):
        for end in range(start + 1, len(s) + 1):
            substr = s[start:end]
            reverse = substr[::-1]
            if substr == reverse and answer < len(substr):
                answer = len(substr)

    return answer
