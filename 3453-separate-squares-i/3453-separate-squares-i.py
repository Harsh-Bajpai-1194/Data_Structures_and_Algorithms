class Solution(object):
    def separateSquares(self, squares):
        """
        :type squares: List[List[int]]
        :rtype: float
        """
        total_area = sum(float(l) * l for x, y, l in squares)
        target = total_area / 2.0
        low = float(min(y for x, y, l in squares))
        high = float(max(y + l for x, y, l in squares))
        for i in range(100):
            mid = (low + high) / 2.0
            area_below = 0.0
            for x, y, l in squares:
                if mid > y:
                    h_below = min(float(l), mid - y)
                    area_below += h_below * l
            if area_below < target: low = mid
            else: high = mid
        return low