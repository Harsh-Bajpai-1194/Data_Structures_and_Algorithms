class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import math
        element_sum,digit_sum=0,0
        for i in range(len(nums)):
            element_sum+=nums[i]
            while(nums[i]!=0):
                digit=nums[i]%10
                nums[i]//=10
                digit_sum+=digit
        return abs(element_sum-digit_sum)