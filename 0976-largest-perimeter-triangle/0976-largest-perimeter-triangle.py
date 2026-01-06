class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        perimeter=0
        for i in range(len(nums)-2):
            if nums[i]<nums[i+1]+nums[i+2] and nums[i+1]<nums[i]+nums[i+2] and nums[i+2]<nums[i+1]+nums[i] and sum(nums[i:i+3])>perimeter: perimeter=sum(nums[i:i+3])
        return perimeter