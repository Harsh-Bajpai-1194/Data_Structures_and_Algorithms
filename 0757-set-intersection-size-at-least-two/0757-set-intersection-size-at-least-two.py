class Solution(object):
    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: (x[1], -x[0]))
        p1, p2 = -1, -1
        count = 0
        for s, e in intervals:
            if s > p2:
                count += 2
                p1 = e - 1
                p2 = e
            elif s > p1:
                count += 1
                p1 = p2
                p2 = e
        return count