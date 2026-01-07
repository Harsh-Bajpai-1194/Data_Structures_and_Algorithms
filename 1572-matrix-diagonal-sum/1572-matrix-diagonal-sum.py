class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        sum=0
        a=len(mat)//2
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i==j: sum+=mat[i][j]
            mat[i]=mat[i][-1::-1]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i==j: sum+=mat[i][j]
        return sum if len(mat)%2==0 else sum-mat[a][a]