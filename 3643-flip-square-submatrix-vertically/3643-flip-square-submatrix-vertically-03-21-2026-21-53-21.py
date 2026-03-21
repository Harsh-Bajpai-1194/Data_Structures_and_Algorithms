class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        a,b=x,x+k-1
        while a < b:
            for j in range(y, y + k):
                grid[a][j], grid[b][j] = grid[b][j], grid[a][j]
            a, b = a + 1, b - 1
        return grid