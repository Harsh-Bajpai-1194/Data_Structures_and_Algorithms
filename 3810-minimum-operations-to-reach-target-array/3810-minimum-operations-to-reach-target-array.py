class Solution(object):
    def minOperations(self, nums, target):
        """
        :type nums: List[int]
        :type target: List[int]
        :rtype: int
        """
        c,L=0,set()
        for i in range(len(nums)):
            if (nums[i]!=target[i] and (i==0 or (nums[i],target[i])!=(nums[i-1],target[i-1])) and nums[i] not in L):
                c+=1
                L.add(nums[i])
        return c