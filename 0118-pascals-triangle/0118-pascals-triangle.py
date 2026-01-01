class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        L,L1,N=[],[],numRows
        for i in range(1,N+1):
            a=1
            L1=[]
            for j in range(1,i+1):
                L1.append(a)
                a=int(a*(i-j)/j)
            L.append(L1)
        return L