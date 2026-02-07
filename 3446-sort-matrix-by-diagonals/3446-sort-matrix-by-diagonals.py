class Solution(object):
    def sortMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(grid)
        for k in range(-(n-1), n):
            vals = []
            i = max(0, k)
            j = i - k
            while i < n and j < n:
                vals.append(grid[i][j])
                i += 1
                j += 1
            vals.sort(reverse=(k >= 0))
            i = max(0, k)
            j = i - k
            t = 0
            while i < n and j < n:
                grid[i][j] = vals[t]
                i += 1
                j += 1
                t += 1
        return grid