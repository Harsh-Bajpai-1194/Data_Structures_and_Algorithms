class Solution(object):
    def countCoveredBuildings(self, n, buildings):
        """
        :type n: int
        :type buildings: List[List[int]]
        :rtype: int
        """
        min_r = [float('inf')] * (n + 1)
        max_r = [float('-inf')] * (n + 1)
        min_c = [float('inf')] * (n + 1)
        max_c = [float('-inf')] * (n + 1)
        for r, c in buildings:
            if c < min_r[r]: min_r[r] = c
            if c > max_r[r]: max_r[r] = c
            if r < min_c[c]: min_c[c] = r
            if r > max_c[c]: max_c[c] = r
        ans = 0
        for r, c in buildings:
            if min_r[r] < c and max_r[r] > c and min_c[c] < r and max_c[c] > r: ans += 1
        return ans