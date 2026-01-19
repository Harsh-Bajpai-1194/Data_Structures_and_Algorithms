class Solution(object):
    def maxRunTime(self, n, batteries):
        """
        :type n: int
        :type batteries: List[int]
        :rtype: int
        """
        batteries.sort()
        s=sum(batteries)
        while batteries[-1]>s//n:
            n-=1
            s-=batteries.pop()
        return s//n