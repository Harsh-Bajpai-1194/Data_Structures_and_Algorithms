class Solution(object):
    def mirrorDistance(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=int(str(n)[-1::-1])
        return abs(n-a)