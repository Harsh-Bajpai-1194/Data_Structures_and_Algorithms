class Solution(object):
    def minScoreTriangulation(self, values):
        """
        :type values: List[int]
        :rtype: int
        """
        n = len(values)
        L=[[0] * n for i in range(n)]
        for l in range(2, n):  
            for i in range(n - l):
                j=i+l
                L[i][j] = float('inf')
                for k in range(i + 1, j): L[i][j] = min(L[i][j],L[i][k] + L[k][j] + values[i] * values[j] * values[k])
        return L[0][n-1]