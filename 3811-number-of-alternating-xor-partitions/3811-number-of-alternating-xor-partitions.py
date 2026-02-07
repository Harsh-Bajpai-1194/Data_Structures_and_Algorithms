class Solution(object):
    def alternatingXOR(self, nums, target1, target2):
        """
        :type nums: List[int]
        :type target1: int
        :type target2: int
        :rtype: int
        """
        L1,L2={0:1},{}
        a=b=c=0
        for i in nums:
            a=a^i
            c=L1.get(a^target1,0)
            b=L2.get(a^target2,0)
            if c>0: 
                L2[a]=(L2.get(a,0)+c)
                L2[a]%=10**9+7
            if b>0:
                L1[a]=(L1.get(a,0)+b)
                L1[a]%=10**9+7
        return (b+c)%(10**9+7)
                