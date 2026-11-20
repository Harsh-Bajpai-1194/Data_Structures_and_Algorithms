class Solution(object):
    def maxSelectedElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        b = k = p = 1
        l = -10
        for x in sorted(nums):
            d = x - l
            if d == 0:
                p = k + 1
            elif d == 1:
                k, p = k + 1, p + 1
            elif d == 2:
                k, p = p + 1, 1
            else:
                k = p = 1
            b, l = max(b, k, p), x
        return b