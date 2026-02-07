class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        L=[]
        for i in range(min(nums),max(nums)):
            if i not in nums: L.append(i)
        return sorted(L)