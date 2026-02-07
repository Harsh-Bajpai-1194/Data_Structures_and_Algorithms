class Solution(object):
    def findMaxVal(self, n, restrictions, diff):
        """
        :type n: int
        :type restrictions: List[List[int]]
        :type diff: List[int]
        :rtype: int
        """
        L=None
        L=[0]+[float('inf')]*(n-1)
        for i, j in restrictions:
            if j<L[i]:
                L[i]=j
        for i in range(n-1):
            if L[i+1]>L[i]+diff[i]:
                L[i+1]=L[i]+diff[i]
        for i in range(n-2,-1,-1):
            if L[i+1]+diff[i]<L[i]:
                L[i]=L[i+1]+diff[i]
        return max(L)