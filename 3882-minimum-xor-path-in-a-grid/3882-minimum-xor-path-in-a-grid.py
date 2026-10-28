class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        R=len(grid); C=len(grid[0]); dp=[]
        for i in range(R):
            dp.append([set() for i in range(C)])
        dp[0][0].add(grid[0][0])
        for i in range(R):
            for j in range(C):
                if i==0 and j==0:
                    continue
                if i>0:
                    for k in dp[i-1][j]:
                        dp[i][j].add(k^grid[i][j])
                if j>0:
                    for k in dp[i][j-1]:
                        dp[i][j].add(k^grid[i][j])
        return min(dp[R-1][C-1])