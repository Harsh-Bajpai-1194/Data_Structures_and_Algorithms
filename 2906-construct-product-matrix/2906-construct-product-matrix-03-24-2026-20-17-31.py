class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        m, n = len(grid), len(grid[0])
        ans = [[0] * n for i in range(m)]
        prefix = 1
        for i in range(m):
            for j in range(n):
                ans[i][j] = prefix
                prefix = prefix * grid[i][j] % MOD
        suffix = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                ans[i][j] = ans[i][j] * suffix % MOD
                suffix = suffix * grid[i][j] % MOD
        return ans