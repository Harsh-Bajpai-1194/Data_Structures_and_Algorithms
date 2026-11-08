class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        row_c = [0] * m
        col_c = [0] * n
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_c[i] += 1
                    col_c[j] += 1
        c = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if row_c[i] > 1 or col_c[j] > 1:
                        c += 1
        return c