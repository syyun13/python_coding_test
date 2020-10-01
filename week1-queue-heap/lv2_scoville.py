# Level 2 Coding Challenge:
# Leo wants to make all foods to have the scoville scale of at least K.
# Leo can mix two of the lowest scoville foods to create a new food.
# mixed food's scoville scale = lowest scoville scale + (second lowest scoville scale * 2)
# Leo continues to mix until all foods have higher scoville scale than K.
# When given an array of all foods 'scoville' and the number 'K',
# find the least number of mixing that Leo should complete to make all foods' scoville scale is higher than or equal to K.

import heapq
def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        min1 = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville)
        heapq.heappush(scoville, min1 + (min2 * 2))
        answer += 1
    
    return answer
