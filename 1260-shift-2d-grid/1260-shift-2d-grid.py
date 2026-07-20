class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        total = m * n
        k %= total
        L = [[0] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                x = i * n + j
                y = (x + k) % total
                R = y // n
                C = y % n
                L[R][C] = grid[i][j]
        return L