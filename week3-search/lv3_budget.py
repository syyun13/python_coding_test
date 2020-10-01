# Level 3 Coding Challenge:
# Conditions for distributing the budget:
# 1. If all requests can be fulfilled, distribute the exact amount that was requested.
# 2. If all requests cannot be fulfilled, set an upper limit.
# All requests smaller than the limit will receive the full amount
# while all requests larger will only be given the limited amount.
# 'budgets' is an array of all requests and 'M' is the total budget.
# Return a upper limit that follows the given condition.

def solution(budgets, M):
    answer = 0
    budgets.sort()

    total = sum(budgets)
    if total <= M:
        return budgets[-1]

    min_budget = 1
    max_budget = budgets[-1]
    recent_midpoint = 0

    while min_budget <= max_budget:
        midpoint = int( (min_budget + max_budget) / 2 )
        current_sum = sum([min(midpoint, budget) for budget in budgets])
        if recent_midpoint == midpoint:
            return midpoint
        if current_sum > M:
            max_budget = midpoint - 1
        else:
            answer = midpoint
            min_budget = midpoint + 1
        recent_midpoint = midpoint

    return answer
