class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_dp = [[0]*n for i in range(m)]
        min_dp = [[0]*n for i in range(m)]
        max_dp[0][0] = min_dp[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0: continue
                vals = []
                if i > 0: vals += [max_dp[i-1][j] * grid[i][j], min_dp[i-1][j] * grid[i][j]]
                if j > 0: vals += [max_dp[i][j-1] * grid[i][j], min_dp[i][j-1] * grid[i][j]]
                max_dp[i][j] = max(vals)
                min_dp[i][j] = min(vals)
        return max_dp[-1][-1] % (10**9 + 7) if max_dp[-1][-1] >= 0 else -1