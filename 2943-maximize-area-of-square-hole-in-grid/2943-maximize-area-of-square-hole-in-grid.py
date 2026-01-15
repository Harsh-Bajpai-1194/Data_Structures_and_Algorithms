class Solution(object):
    def maximizeSquareHoleArea(self, n, m, hBars, vBars):
        """
        :type n: int
        :type m: int
        :type hBars: List[int]
        :type vBars: List[int]
        :rtype: int
        """
        def get_max_gap(bars):
            bars.sort()
            max_consecutive = 1
            current_consecutive = 1
            for i in range(1, len(bars)):
                if bars[i] == bars[i-1] + 1: current_consecutive += 1
                else: current_consecutive = 1
                max_consecutive = max(max_consecutive, current_consecutive)
            return max_consecutive + 1
        side=min(get_max_gap(hBars),get_max_gap(vBars))
        return side**2