class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        diff = [[0] * (n + 1) for _ in range(n + 1)]
        for r1, c1, r2, c2 in queries:
            diff[r1][c1] += 1
            diff[r1][c2 + 1] -= 1
            diff[r2 + 1][c1] -= 1
            diff[r2 + 1][c2 + 1] += 1
        mat = [[0] * n for _ in range(n)]
        for r in range(n):
            row_sum = 0
            for c in range(n):
                row_sum += diff[r][c]
                if r > 0: mat[r][c] = row_sum + mat[r-1][c]
                else: mat[r][c] = row_sum
        return mat