class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        count = k
        for num in nums:
            if num == 1:
                if count < k: return False
                count = 0
            else: count += 1
        return True