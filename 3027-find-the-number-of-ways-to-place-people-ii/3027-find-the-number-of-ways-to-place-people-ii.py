class Solution(object):
    def numberOfPairs(self, points):
        ans = 0
        points.sort(key=lambda x: (x[0], -x[1]))
        for i, (xi, yi) in enumerate(points):
            maxY = -10**10
            for j in range(i + 1, len(points)):
                xj, yj = points[j]
                if yi >= yj > maxY:
                    ans += 1
                    maxY = yj
        return ans