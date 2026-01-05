class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        total=count=0
        minimum=float('inf')
        for i in matrix:
            for j in i:
                if j<0: count+=1
                total+=abs(j)
                minimum=min(minimum,abs(j))
        if (count%2==0): return total
        return total-(2*minimum)