class Solution(object):
    def longestBalanced(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum=0
        for i in range(len(nums)):
            odd,even=set(),set()
            for j in range(i,len(nums)):
                if (nums[j]&1): odd.add(nums[j])
                else: even.add(nums[j])
                if (len(even)==len(odd)):
                    maximum=max(maximum,j-i+1)
        return maximum