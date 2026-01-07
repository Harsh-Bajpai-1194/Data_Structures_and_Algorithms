class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        total,a,b=0,0,len(nums)
        for x in nums: total+=x
        rem=total%p
        if rem==0: return 0
        d={0:-1}
        for i in range(len(nums)):
            a=(a+nums[i])%p
            c=(a-rem)%p
            if c in d: b=min(b,i-d[c])
            d[a]=i
        if b<len(nums): return b
        return -1