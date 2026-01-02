class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L=[]
        for i in matrix: L=L+i
        if target in L: return True
        return False