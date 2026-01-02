class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        L={}
        for i,j in enumerate(nums):
            if j in L and (i-L[j])<=k: return True
            L[j]=i
        return False