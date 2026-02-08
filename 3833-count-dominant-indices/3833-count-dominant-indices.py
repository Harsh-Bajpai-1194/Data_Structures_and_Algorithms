class Solution(object):
    def dominantIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c,sum,x=0,0,0
        for i in range(len(nums)-1,-1,-1):
            if x>0:
                if x*nums[i]>sum: c+=1
            sum,x=sum+nums[i],x+1
        return c