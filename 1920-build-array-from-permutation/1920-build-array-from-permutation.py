class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        L=[]
        for i in range(len(nums)):
            L.append(nums[nums[i]])
        return L