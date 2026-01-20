class Solution(object):
    def findSmallestInteger(self, nums, value):
        """
        :type nums: List[int]
        :type value: int
        :rtype: int
        """
        count = [0] * value
        for x in nums:
            count[x % value] += 1
        mex = 0
        while True:
            rem = mex % value
            if count[rem] == 0:
                return mex
            count[rem] -= 1
            mex += 1