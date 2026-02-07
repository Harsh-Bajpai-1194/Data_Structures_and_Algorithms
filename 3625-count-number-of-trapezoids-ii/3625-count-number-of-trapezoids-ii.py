class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    def countTrapezoids(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        n = len(points)
        slope_map = defaultdict(lambda: defaultdict(int))
        mid_map = defaultdict(lambda: defaultdict(int))
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                dy = y2 - y1
                dx = x2 - x1
                g = self.gcd(dy, dx)
                dy //= g
                dx //= g
                if dx < 0 or (dx == 0 and dy < 0):
                    dx = -dx
                    dy = -dy
                slope = (dx, dy)
                intercept = dy * x1 - dx * y1
                slope_map[slope][intercept] += 1
                mid = (x1 + x2, y1 + y2)
                mid_map[mid][slope] += 1
        ans = 0
        for slope in slope_map:
            group = slope_map[slope]
            total_lines = 0
            collinear_pairs = 0
            for count in group.values():
                total_lines += count
                collinear_pairs += count * (count - 1) // 2
            valid_pairs = total_lines * (total_lines - 1) // 2 - collinear_pairs
            ans += valid_pairs
        for mid in mid_map:
            group = mid_map[mid]
            total_lines = 0
            same_slope_pairs = 0
            for count in group.values():
                total_lines += count
                same_slope_pairs += count * (count - 1) // 2
            valid_parallelograms = total_lines * (total_lines - 1) // 2 - same_slope_pairs
            ans -= valid_parallelograms
        return ans