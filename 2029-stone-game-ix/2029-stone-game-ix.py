class Solution(object):
    def stoneGameIX(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        L=[0]*3
        for i in stones: L[i%3]+=1
        if ~L[0]&1: return min(L[1],L[2])>=1
        return abs(L[1]-L[2])>=3