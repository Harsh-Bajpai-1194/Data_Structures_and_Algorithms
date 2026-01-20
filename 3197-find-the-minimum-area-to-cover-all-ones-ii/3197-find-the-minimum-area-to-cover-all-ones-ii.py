class Solution(object):
    def minimumSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        g = grid
        m, n = len(g), len(g[0])

        def A(r1, r2, c1, c2):
            cells = [(i, j) for i in range(r1, r2) for j in range(c1, c2) if g[i][j]]
            if not cells:
                return 0
            rs, cs = zip(*cells)
            return (max(rs) - min(rs) + 1) * (max(cs) - min(cs) + 1)

        ans = float('inf')

        for c1 in range(1, n - 1):
            for c2 in range(c1 + 1, n):
                a, b, c = A(0, m, 0, c1), A(0, m, c1, c2), A(0, m, c2, n)
                if a and b and c:
                    ans = min(ans, a + b + c)

        for r1 in range(1, m - 1):
            for r2 in range(r1 + 1, m):
                a, b, c = A(0, r1, 0, n), A(r1, r2, 0, n), A(r2, m, 0, n)
                if a and b and c:
                    ans = min(ans, a + b + c)

        for r in range(1, m):
            for c in range(1, n):
                rects_list = [
                    (A(0, r, 0, c), A(0, r, c, n), A(r, m, 0, n)),
                    (A(0, r, 0, n), A(r, m, 0, c), A(r, m, c, n)),
                    (A(0, r, 0, c), A(r, m, 0, c), A(0, m, c, n)),
                    (A(0, m, 0, c), A(0, r, c, n), A(r, m, c, n))
                ]
                for rects in rects_list:
                    if all(rects):
                        ans = min(ans, sum(rects))

        return ans if ans != float('inf') else 0