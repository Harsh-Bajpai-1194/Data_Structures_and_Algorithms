class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        L = triangle[-1][:]
        for i in range(len(triangle)-2,-1,-1):
            for j in range(len(triangle[i])):
                L[j]=triangle[i][j]+min(L[j],L[j+1])
        return L[0]