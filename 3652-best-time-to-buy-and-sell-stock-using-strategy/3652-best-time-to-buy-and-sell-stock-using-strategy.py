class Solution(object):
    def maxProfit(self, prices, strategy, k):
        """
        :type prices: List[int]
        :type strategy: List[int]
        :type k: int
        :rtype: int
        """
        n = len(prices)
        current_profit = 0
        for p, s in zip(prices, strategy): current_profit += p * s
        prefix_s = [0] * (n + 1)
        prefix_p = [0] * (n + 1)
        for i in range(n):
            prefix_s[i+1] = prefix_s[i] + (strategy[i] * prices[i])
            prefix_p[i+1] = prefix_p[i] + prices[i]
        max_gain = 0
        half_k = k // 2
        for i in range(n - k + 1):
            original_sub_profit = prefix_s[i+k] - prefix_s[i]
            new_sub_profit = prefix_p[i+k] - prefix_p[i + half_k]
            gain = new_sub_profit - original_sub_profit
            if gain > max_gain: max_gain = gain
        return current_profit + max_gain