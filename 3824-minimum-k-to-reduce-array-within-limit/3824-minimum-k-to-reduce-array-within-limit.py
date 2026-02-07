class Solution(object):
    def minimumK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l,r,c=1,max(nums)+len(nums),max(nums)+len(nums)
        while (l<=r):
            mid=(l+r)>>1
            count=0
            for i in nums:
                count+=(i+mid-1)//mid    
            if count<=mid**2:
                c=mid
                r=mid-1
            else: l=mid+1
        return c