class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                t = a * a + b * b
                if t > n * n: break
                c = int(t ** 0.5)
                if c * c == t: count += 1
        return count