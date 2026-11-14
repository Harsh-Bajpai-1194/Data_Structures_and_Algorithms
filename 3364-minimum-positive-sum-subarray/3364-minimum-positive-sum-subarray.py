class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: int
        :type r: int
        :rtype: int
        """
        n = len(nums) 
        best = float('inf') 
        for length in range(l, r + 1): 
            for i in range(n - length + 1): 
                s = sum(nums[i:i + length]) 
                if 0 < s < best: 
                    best = s 
        return -1 if best == float('inf') else best