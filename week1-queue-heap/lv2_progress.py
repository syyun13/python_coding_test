# Level 2 Coding Challenge:
# The team is working on a functional improvement.
# Each feature can only be reflected in the service when it is 100% completed.
# Because each feature is developed with a different speed,
# a feature behind it can be developed before the feature in front of it
# which will be distributed together when the function in front of it is being distributed.
# 'progresses' is an array of integers with the progress level of each feature in order of distribution
# 'speeds' is an array of each feature's development speed.
# Return an array of integers that shows how many features will be distributed at each distribution.

def solution(progresses, speeds):
    answer = []

    days = []
    total = len(progresses)

    progress_speed = zip(progresses, speeds)
    
    for progress, speed in progress_speed:
        w = 100 - progress
        day = -(-w // speed)
        days.append(day)

    max = days[0]
    count = 1
    i = 1
    
    while i < total:
        if days[i] <= max:
            count += 1
        else:
            answer.append(count)
            count = 1
            max = days[i]
        i += 1
    
    answer.append(count)
    
    return answer
