# Level 2 Coding Challenge:
# When given string 's', find a substring of s that comes at the last when they are sorted in dictionary order.
# Order of each character in the given string cannot change when creating a substring.
# string s is only made of lower case characters.
# ex. If s = "yxyc", the function will return "yyc".

def solution(s):
    answer = ''

    sorted_char = sorted([(char, index * -1) for index, char in enumerate(list(s), 0)])

    last_char, last_i = sorted_char.pop()

    answer += last_char

    while len(sorted_char) > 0:
        char, i = sorted_char.pop()
        if i < last_i:
            answer += char
            last_i = i

    return answer
