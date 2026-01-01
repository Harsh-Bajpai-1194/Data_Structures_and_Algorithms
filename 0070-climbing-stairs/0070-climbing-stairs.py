class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a,b,sum=0,1,0
        for i in range(1,n+1):
            sum=a+b
            a=b
            b=sum
        return sum