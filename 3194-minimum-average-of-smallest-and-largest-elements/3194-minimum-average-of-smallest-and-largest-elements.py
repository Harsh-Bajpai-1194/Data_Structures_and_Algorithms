class Solution(object):
    def minimumAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: float
        """
        L=[]
        while(nums!=[]):
            L.append((max(nums)+min(nums))/2.0)
            nums.remove(max(nums))
            nums.remove(min(nums))
        return min(L)