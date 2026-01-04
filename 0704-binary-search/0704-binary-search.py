class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i,j=0,len(nums)-1
        while i<=j:
            mid=(i+j)>>1
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                i=mid+1
            else:
                j=mid-1
        return -1