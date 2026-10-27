class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid=[['#']*n for i in range(m)]
        for j in range(n):
            grid[0][j]='.'
        for i in range(1,m):
            grid[i][n-1]="."
        return ["".join(i) for i in grid]