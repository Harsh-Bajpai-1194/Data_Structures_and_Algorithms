class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        from collections import Counter
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        counts = []
        for s in strs:
            c = Counter(s)
            counts.append((c['0'], c['1']))
        for zeros, ones in counts:
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1): 
                    dp[i][j] = max(dp[i][j],1 + dp[i - zeros][j - ones])
        return dp[m][n]