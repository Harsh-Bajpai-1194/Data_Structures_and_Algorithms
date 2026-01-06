class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        n = len(strs)
        m = len(strs[0])
        dp = [1] * m
        for i in range(m):
            for j in range(i):
                valid = True
                for k in range(n):
                    if strs[k][j] > strs[k][i]:
                        valid = False
                        break
                if valid: dp[i] = max(dp[i], dp[j] + 1)
        return m - max(dp)