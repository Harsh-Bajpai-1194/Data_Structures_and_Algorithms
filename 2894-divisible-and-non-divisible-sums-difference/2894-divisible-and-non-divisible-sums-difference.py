class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        total_sum=n*(n+1)//2  
        divisible_sum=0
        for i in range(m,n+1,m): divisible_sum+=i  
        return total_sum-2*divisible_sum