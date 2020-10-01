# Level 3 Coding Challenge:
# Game users teamed up to hunt the monster.
# They want to increase the power of attack by using items for the characters in the team.
# Items in this game increase the character's power, while decreasing his/her energy.
# Users can choose to use an item or not, but an item can only be used when the character has more energy than 100.
# Only one item can be used per character and used item will disappear.
# 'healths' is an array of each character's current energy.
# 'items' is an array of each item's effect. (increase in power, decrease in energy)
# Return an array that tells which item should be used on which character to maximize the team's power.

import heapq
from collections import deque

def solution(healths, items):
    answer = []
    healths.sort()

    BUFF, DEBUFF, INDEX = 0, 1, 2

    item_list = []
    for i, item in enumerate(items, 1):
        item_list.append([-1 * item[BUFF], item[DEBUFF], i])
    item_list.sort(key=lambda x: x[DEBUFF])
    item_list = deque(item_list)

    usable_list = []

    for health in healths:
        while item_list and health - item_list[0][DEBUFF] >= 100:
            item = item_list.popleft()
            heapq.heappush(usable_list, [item[BUFF], item[INDEX]])
        if usable_list:
            use_item = heapq.heappop(usable_list)
            answer.append(use_item[1])

    answer.sort()
    return answer
