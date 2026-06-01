class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.sort(reverse=True)
        sum = 0
        n = len(cost)
        for i in range(n):
            if i % 3 != 2: sum = sum + cost[i]
        return sum