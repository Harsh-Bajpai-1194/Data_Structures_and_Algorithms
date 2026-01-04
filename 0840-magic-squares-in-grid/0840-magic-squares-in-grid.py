class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        count = 0
        for r in range(rows - 2):
            for c in range(cols - 2):
                if grid[r+1][c+1] != 5: continue
                subgrid = [grid[r+i][c+j] for i in range(3) for j in range(3)]
                if sorted(subgrid) != [1, 2, 3, 4, 5, 6, 7, 8, 9]: continue
                if (grid[r][c] + grid[r][c+1] + grid[r][c+2] == 15 and
                    grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2] == 15 and
                    grid[r][c] + grid[r+1][c] + grid[r+2][c] == 15 and
                    grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] == 15 and
                    grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] == 15 and
                    grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] == 15):
                    count += 1
        return count