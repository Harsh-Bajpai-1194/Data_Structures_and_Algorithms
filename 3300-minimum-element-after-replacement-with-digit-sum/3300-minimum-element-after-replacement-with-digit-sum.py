class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            sum=0
            while(nums[i]!=0):
                sum+=nums[i]%10
                nums[i]//=10
            nums[i]=sum
        return min(nums)