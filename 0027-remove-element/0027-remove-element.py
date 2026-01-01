class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i=0
        j=len(nums)-1
        while (i<=j):
            if nums[i]==val:
                nums[i],nums[j]=nums[j],nums[i]
                j=j-1
            else: i=i+1
        return i