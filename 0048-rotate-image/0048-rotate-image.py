class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix[0])
        matrix[:]=matrix[-1::-1]
        for i in range(n):
            L=[]
            for j in range(n):
                L.append(matrix[j][i])
            matrix.append(L)
        matrix[:]=matrix[n:]