class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zi=0
        for i in range(len(nums)):
            if (nums[i]!=0):
                nums[zi]=nums[i]
                zi+=1
        while (zi<len(nums)):
            nums[zi]=0
            zi+=1