class Solution(object):
    def numberOfPairs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key=lambda x: (x[0], -x[1]))
        ans = 0
        n = len(points)
        for i in range(n):
            maxy = -10**9
            yi = points[i][1]
            for j in range(i+1, n):
                yj = points[j][1]
                if yi >= yj and yj > maxy:
                    ans += 1
                    maxy = yj
        return ans