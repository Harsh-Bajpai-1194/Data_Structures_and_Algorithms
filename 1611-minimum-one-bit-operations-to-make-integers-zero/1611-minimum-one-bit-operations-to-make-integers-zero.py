class Solution(object):
    def minimumOneBitOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0: return 0
        k,c=0,1
        while(c*2<=n): c,k=c*2,k+1
        return pow(2,k+1)-self.minimumOneBitOperations(n^c)-1