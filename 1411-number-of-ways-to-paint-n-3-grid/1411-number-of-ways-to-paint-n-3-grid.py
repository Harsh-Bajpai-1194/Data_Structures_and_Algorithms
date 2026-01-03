class Solution(object):
    def numOfWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD=10**9+7
        aba=abc=6
        for i in range(n-1):
            aba1=(3*aba+2*abc)%MOD
            abc1=(2*aba+2*abc)%MOD
            aba,abc=aba1,abc1
        return (aba+abc)%MOD