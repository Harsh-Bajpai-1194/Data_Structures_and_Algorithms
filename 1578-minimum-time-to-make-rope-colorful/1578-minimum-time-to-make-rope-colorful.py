class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        total_time = 0
        n = len(colors)
        for i in range(1, n):
            if colors[i] == colors[i-1]:
                total_time += min(neededTime[i], neededTime[i-1])
                neededTime[i] = max(neededTime[i], neededTime[i-1])
        return total_time