class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        if 0 in nums:
            return 0
        for i in range(len(nums)):
            if nums[i]<0:
                count+=1
        if count%2==0:
            return 1
        else:
            return -1