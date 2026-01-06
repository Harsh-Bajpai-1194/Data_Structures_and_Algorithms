class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        L=[nums[0]]
        for i in range(1,len(nums)):
            if index[i]>=len(L): L.append(nums[i])
            else: L.insert(index[i],nums[i])
        return L