class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """
        import heapq
        h = []
        for p, t in classes:
            gain = (float(p+1)/(t+1)) - (float(p)/t)
            heapq.heappush(h, (-gain, p, t))
        for i in range(extraStudents):
            g, p, t = heapq.heappop(h)
            p, t = p+1, t+1
            gain = (float(p+1)/(t+1)) - (float(p)/t)
            heapq.heappush(h, (-gain, p, t))
        total = 0.0
        for i, p, t in h:
            total += float(p)/t
        return total/len(classes)