class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = [0, -9000000000, -9000000000] 
        for i in nums:
            for x in L[:]: L[(x+i)%3] = max(L[(x+i)%3], x+i)
        return L[0]