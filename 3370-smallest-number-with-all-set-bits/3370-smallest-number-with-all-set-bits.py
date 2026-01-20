class Solution(object):
    def smallestNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in range(n,10000):
            if str(bin(i))[2:].count("0")==0: return i