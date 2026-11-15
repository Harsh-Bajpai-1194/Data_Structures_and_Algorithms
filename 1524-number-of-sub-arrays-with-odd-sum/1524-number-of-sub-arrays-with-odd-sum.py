class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        MOD=10**9+7
        odd,even=0,1
        prefix,ans=0,0
        for i in arr:
            prefix+=i
            if prefix%2==0:
                ans+=odd
                even+=1
            else:
                ans+=even
                odd+=1
        ans%=MOD
        return int(ans)