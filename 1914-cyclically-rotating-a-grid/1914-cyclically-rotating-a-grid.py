class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        from typing import List
        m, n = len(grid), len(grid[0])
        for i in range(min(m, n) // 2):
            top, bottom, left, right = i, m-i-1, i, n-i-1
            coordinates = [(top, j) for j in range(left, right)]
            coordinates += [(i, right) for i in range(top, bottom)]
            coordinates += [(bottom, j) for j in range(right, left, -1)]
            coordinates += [(i, left) for i in range(bottom, top, -1)]
            L = [grid[r][c] for r, c in coordinates]
            shift = k % len(L)
            for i, (r, c) in enumerate(coordinates):
                grid[r][c] = L[(i + shift) % len(L)]
        return grid