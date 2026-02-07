class Solution(object):
    def maximumProfit(self, prices, k):
        """
        :type prices: List[int]
        :type k: int
        :rtype: int
        """
        if not prices or k == 0: return 0
        n = len(prices)
        dp = [[0, -float('inf'), -float('inf')] for i in range(k + 1)]
        for j in range(1, k + 1):
            dp[j][1] = -prices[0]
            dp[j][2] = prices[0]
        for i in range(1, n):
            next_dp = [row[:] for row in dp]
            for j in range(1, k + 1):
                next_dp[j][0] = max(dp[j][0], dp[j][1] + prices[i], dp[j][2] - prices[i])
                next_dp[j][1] = max(dp[j][1], dp[j-1][0] - prices[i])
                next_dp[j][2] = max(dp[j][2], dp[j-1][0] + prices[i])
            dp = next_dp
        return dp[k][0]