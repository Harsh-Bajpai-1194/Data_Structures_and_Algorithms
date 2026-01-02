class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        L=[]
        for i in matrix: L+=i
        if target in L: return True
        return False