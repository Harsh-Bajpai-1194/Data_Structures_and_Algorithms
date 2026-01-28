class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        n=list(n)
        n.sort()
        n="".join(n)
        return int(n[-1])