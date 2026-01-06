class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        L=[0]*60
        c=0
        for i in time:
            a=i%60
            complement=(60-a)%60
            c+=L[complement]
            L[a]=L[a]+1
        return c