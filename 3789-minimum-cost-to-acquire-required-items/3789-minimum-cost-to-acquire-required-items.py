class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        if cost1 + cost2 <= costBoth:
            return cost1 * need1 + cost2 * need2
        c = min(need1, need2)
        totalCost = c * costBoth
        need1 -= c
        need2 -= c
        if need1 > 0:
            totalCost += need1 * min(cost1, costBoth)
        elif need2 > 0:
            totalCost += need2 * min(cost2, costBoth)
        return totalCost