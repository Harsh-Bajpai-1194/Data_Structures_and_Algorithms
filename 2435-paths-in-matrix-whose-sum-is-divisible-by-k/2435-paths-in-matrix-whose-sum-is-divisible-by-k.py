class Solution(object):
    def numberOfPaths(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        dp = [[[0] * k for i in range(n)] for j in range(m)]
        dp[0][0][grid[0][0] % k] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0: continue
                val = grid[i][j]
                for r in range(k):
                    prev_rem = (r - val) % k
                    ways = 0
                    if i > 0: ways += dp[i-1][j][prev_rem]
                    if j > 0: ways += dp[i][j-1][prev_rem]
                    dp[i][j][r] = ways % MOD
        return dp[m-1][n-1][0]